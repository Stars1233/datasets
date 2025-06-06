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

"""The Multi-Genre NLI Corpus."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@InProceedings{N18-1101,
  author = "Williams, Adina
            and Nangia, Nikita
            and Bowman, Samuel",
  title = "A Broad-Coverage Challenge Corpus for
           Sentence Understanding through Inference",
  booktitle = "Proceedings of the 2018 Conference of
               the North American Chapter of the
               Association for Computational Linguistics:
               Human Language Technologies, Volume 1 (Long
               Papers)",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  pages = "1112--1122",
  location = "New Orleans, Louisiana",
  url = "http://aclweb.org/anthology/N18-1101"
}
"""

_DESCRIPTION = """\
The Multi-Genre Natural Language Inference (MultiNLI) corpus is a
crowd-sourced collection of 433k sentence pairs annotated with textual
entailment information. The corpus is modeled on the SNLI corpus, but differs in
that covers a range of genres of spoken and written text, and supports a
distinctive cross-genre generalization evaluation. The corpus served as the
basis for the shared task of the RepEval 2017 Workshop at EMNLP in Copenhagen.
"""

ROOT_URL = "https://cims.nyu.edu/~sbowman/multinli/multinli_1.0.zip"


class MultiNLIMismatch(tfds.core.GeneratorBasedBuilder):
  """MultiNLI: The Stanford Question Answering Dataset. Version 1.1."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "premise": tfds.features.Text(),
            "hypothesis": tfds.features.Text(),
            "label": tfds.features.Text(),
        }),
        # No default supervised_keys (as we have to pass both premise
        # and hypothesis as input).
        supervised_keys=None,
        homepage="https://www.nyu.edu/projects/bowman/multinli/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    downloaded_dir = dl_manager.download_and_extract(ROOT_URL)
    mnli_path = os.path.join(downloaded_dir, "multinli_1.0")
    train_path = os.path.join(mnli_path, "multinli_1.0_train.txt")

    validation_path = os.path.join(mnli_path, "multinli_1.0_dev_mismatched.txt")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"filepath": train_path}
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION, gen_kwargs={"filepath": validation_path}
        ),
    ]

  def _generate_examples(self, filepath):
    """Generate mnli mismatch examples.

    Args:
      filepath: a string

    Yields:
      dictionaries containing "premise", "hypothesis" and "label" strings
    """
    for idx, line in enumerate(tf.io.gfile.GFile(filepath, "rb")):
      if idx == 0:
        continue
      line = tf.compat.as_text(line.strip())
      split_line = line.split("\t")
      yield idx, {
          "premise": split_line[5],
          "hypothesis": split_line[6],
          "label": split_line[0],
      }
