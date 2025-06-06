# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""Tool to generate the dataset catalog documentation.
"""

import argparse
import collections
import os
from typing import Dict, List, Optional

from absl import app
from absl.flags import argparse_flags
from etils import epath

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import doc_utils
from tensorflow_datasets.scripts.documentation import document_datasets
import yaml


def _parse_flags(_) -> argparse.Namespace:
  """Command line flags."""
  parser = argparse_flags.ArgumentParser(
      prog='build_catalog',
      description='Tool to generate the dataset catalog documentation',
  )
  parser.add_argument(
      '--datasets',
      help=(
          'Comma separated list of datasets to document. None for all datasets.'
      ),
  )
  parser.add_argument(
      '--ds_collections',
      help=(
          'Comma separated list of dataset collections to document. None for '
          'all datasets.'
      ),
  )
  parser.add_argument(
      '--catalog_dir',
      help='Directory path where to generate the catalog. Default to TFDS dir.',
  )
  return parser.parse_args()


def main(args: argparse.Namespace):
  # Note: The automated generation call `build_catalog.build_catalog()`
  # directly, so no code should go in `main()`.

  catalog_dir = args.catalog_dir or os.path.join(
      tfds.core.utils.tfds_write_path(),
      'docs',
      'catalog',
  )

  build_catalog(
      datasets=args.datasets.split(',') if args.datasets else None,
      ds_collections=(
          args.ds_collections.split(',') if args.ds_collections else None
      ),
      catalog_dir=catalog_dir,
  )


def _create_datasets_section_toc(
    section: str,
    builder_docs: List[document_datasets.BuilderDocumentation],
) -> str:
  """Creates the section of the overview.md table of content for datasets."""
  heading = '\n### `%s`\n' % section
  nightly_suffix = ' ' + doc_utils.NightlyDocUtil.icon
  entries = [
      f' * [`{doc.name}`]({doc.filestem}.md)'
      + (doc.is_nightly and nightly_suffix or '')
      for doc in builder_docs
  ]
  return '\n'.join([heading] + entries)


def _create_collections_section_toc(
    collection_docs: List[document_datasets.CollectionDocumentation],
) -> str:
  """Creates the section of the overview.md table of content for collections."""
  heading = '\n## `Dataset Collections`\n'
  entries = [f' * [`{doc.name}`]({doc.name}.md)' for doc in collection_docs]
  return '\n'.join([heading] + entries)


def build_catalog(
    datasets: Optional[List[str]] = None,
    ds_collections: Optional[List[str]] = None,
    *,
    catalog_dir: Optional[epath.PathLike] = None,
    doc_util_paths: Optional[doc_utils.DocUtilPaths] = None,
    toc_relative_path: str = '/datasets/catalog/',
    index_template: Optional[epath.PathLike] = None,
    index_filename: str = 'overview.md',
    dataset_types: Optional[List[tfds.core.visibility.DatasetType]] = None,
    include_collections: bool = True,
) -> None:
  """Document all datasets, including the table of content.

  Args:
    datasets: Lists of dataset to document (all if not set)
    ds_collections: Lists of all dataset collections to document (all if not
      set)
    catalog_dir: Destination path for the catalog
    doc_util_paths: Additional path for visualization, nightly info,...
    toc_relative_path: Relative path of the catalog directory, used to generate
      the table of content relative links.
    index_template: Default template for the index page.
    index_filename: Name of the catalog index file.
    dataset_types: Restrict the generation to the given dataset types. Default
      to all open source non-community datasets
    include_collections: Whether to include dataset collections to the catalog.
      Default to True.
  """
  dataset_types = dataset_types or [
      tfds.core.visibility.DatasetType.TFDS_PUBLIC,
  ]
  tfds.core.visibility.set_availables(dataset_types)

  catalog_dir = tfds.core.Path(catalog_dir)
  index_template = index_template or tfds.core.tfds_path(
      'scripts/documentation/templates/catalog_overview.md'
  )
  index_template = tfds.core.Path(index_template)

  # Iterate over the builder documentations
  section_to_builder_docs = collections.defaultdict(list)
  for builder_doc in document_datasets.iter_documentation_builders(
      datasets, doc_util_paths=doc_util_paths or doc_utils.DocUtilPaths()
  ):
    # Write the builder documentation
    dataset_file = catalog_dir / f'{builder_doc.filestem}.md'
    dataset_file.write_text(builder_doc.content)
    # Save the category
    for section in builder_doc.sections:
      section_to_builder_docs[section].append(builder_doc)

  section_to_collection_docs = collections.defaultdict(list)
  if include_collections:
    # Iterate over the dataset collection documentations
    for collection_doc in document_datasets.iter_collections_documentation(
        ds_collections
    ):
      # Write the dataset collection documentation
      collection_file = catalog_dir / f'{collection_doc.name}.md'
      collection_file.write_text(collection_doc.content)
      # Save the "dataset collection" docs
      section_to_collection_docs['collections'].append(collection_doc)

  _save_table_of_content(
      catalog_dir=catalog_dir,
      section_to_builder_docs=section_to_builder_docs,
      section_to_collection_docs=section_to_collection_docs,
      toc_relative_path=toc_relative_path,
      index_template=index_template,
      index_filename=index_filename,
      include_collections=include_collections,
  )


def _save_table_of_content(
    catalog_dir: tfds.core.Path,
    section_to_builder_docs: Dict[
        str, List[document_datasets.BuilderDocumentation]
    ],
    section_to_collection_docs: Dict[
        str, List[document_datasets.CollectionDocumentation]
    ],
    toc_relative_path: str,
    index_template: tfds.core.Path,
    index_filename: str,
    include_collections: bool,
) -> None:
  """Builds and saves the table of contents (`_toc.yaml` and `overview.md`)."""
  # For _toc.yaml
  toc_yaml = {
      'toc': [{
          'title': 'Overview',
          'path': os.path.join(toc_relative_path, 'overview'),
      }]
  }
  # For overview.md
  toc_overview = []

  # All collections documented, save the table of content
  if include_collections:
    for section, collection_docs in sorted(section_to_collection_docs.items()):
      collection_docs = sorted(collection_docs, key=lambda doc: doc.name)

      # Add `_toc.yaml` section
      sec_dict = {'title': 'Dataset Collections', 'section': []}
      for doc in collection_docs:
        sidebar_item = {
            'path': os.path.join(toc_relative_path, doc.name),
            'title': doc.name,
        }
        sec_dict['section'].append(sidebar_item)
      toc_yaml['toc'].append(sec_dict)

      # Add `overview.md` section
      toc_overview.append(_create_collections_section_toc(collection_docs))

  # All builder documented, save the table of content
  for section, builder_docs in sorted(section_to_builder_docs.items()):
    builder_docs = sorted(builder_docs, key=lambda doc: doc.name)

    # Add `_toc.yaml` section
    sec_dict = {'title': section, 'section': []}
    for doc in builder_docs:
      sidebar_item = {
          'path': os.path.join(toc_relative_path, doc.filestem),
          'title': doc.name + (' (manual)' if doc.is_manual else ''),
      }
      if doc.is_nightly:
        sidebar_item['status'] = 'nightly'
      sec_dict['section'].append(sidebar_item)
    toc_yaml['toc'].append(sec_dict)

    # Add `overview.md` section
    toc_overview.append(_create_datasets_section_toc(section, builder_docs))

  # Write the `overview.md` page
  index_str = index_template.read_text().format(toc='\n'.join(toc_overview))
  catalog_dir.joinpath(index_filename).write_text(index_str)

  # Write the `_toc.yaml` TF documentation navigation bar
  with catalog_dir.joinpath('_toc.yaml').open('w') as f:
    yaml.dump(toc_yaml, f, default_flow_style=False)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)
