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

"""Mathematics database."""

import os

from absl import logging
from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DATA_URL = "https://storage.googleapis.com/mathematics-dataset/mathematics_dataset-v1.0.tar.gz"

_TRAIN_CATEGORY = [
    "train-easy",
    "train-medium",
    "train-hard",
]

_INTERPOLATE_CATEGORY = [
    "interpolate",
]

_MODULES = [
    # extrapolate
    "measurement__conversion",
    # interpolate
    "algebra__linear_1d",
    "algebra__linear_1d_composed",
    "algebra__linear_2d",
    "algebra__linear_2d_composed",
    "algebra__polynomial_roots",
    "algebra__polynomial_roots_composed",
    "algebra__sequence_next_term",
    "algebra__sequence_nth_term",
    "arithmetic__add_or_sub",
    "arithmetic__add_or_sub_in_base",
    "arithmetic__add_sub_multiple",
    "arithmetic__div",
    "arithmetic__mixed",
    "arithmetic__mul",
    "arithmetic__mul_div_multiple",
    "arithmetic__nearest_integer_root",
    "arithmetic__simplify_surd",
    "calculus__differentiate",
    "calculus__differentiate_composed",
    "comparison__closest",
    "comparison__closest_composed",
    "comparison__kth_biggest",
    "comparison__kth_biggest_composed",
    "comparison__pair",
    "comparison__pair_composed",
    "comparison__sort",
    "comparison__sort_composed",
    "measurement__conversion",
    "measurement__time",
    "numbers__base_conversion",
    "numbers__div_remainder",
    "numbers__div_remainder_composed",
    "numbers__gcd",
    "numbers__gcd_composed",
    "numbers__is_factor",
    "numbers__is_factor_composed",
    "numbers__is_prime",
    "numbers__is_prime_composed",
    "numbers__lcm",
    "numbers__lcm_composed",
    "numbers__list_prime_factors",
    "numbers__list_prime_factors_composed",
    "numbers__place_value",
    "numbers__place_value_composed",
    "numbers__round_number",
    "numbers__round_number_composed",
    "polynomials__add",
    "polynomials__coefficient_named",
    "polynomials__collect",
    "polynomials__compose",
    "polynomials__evaluate",
    "polynomials__evaluate_composed",
    "polynomials__expand",
    "polynomials__simplify_power",
    "probability__swr_p_level_set",
    "probability__swr_p_sequence",
    # train-easy train-medium train-hard
    "algebra__linear_1d",
    "algebra__linear_1d_composed",
    "algebra__linear_2d",
    "algebra__linear_2d_composed",
    "algebra__polynomial_roots",
    "algebra__polynomial_roots_composed",
    "algebra__sequence_next_term",
    "algebra__sequence_nth_term",
    "arithmetic__add_or_sub",
    "arithmetic__add_or_sub_in_base",
    "arithmetic__add_sub_multiple",
    "arithmetic__div",
    "arithmetic__mixed",
    "arithmetic__mul",
    "arithmetic__mul_div_multiple",
    "arithmetic__nearest_integer_root",
    "arithmetic__simplify_surd",
    "calculus__differentiate",
    "calculus__differentiate_composed",
    "comparison__closest",
    "comparison__closest_composed",
    "comparison__kth_biggest",
    "comparison__kth_biggest_composed",
    "comparison__pair",
    "comparison__pair_composed",
    "comparison__sort",
    "comparison__sort_composed",
    "measurement__conversion",
    "measurement__time",
    "numbers__base_conversion",
    "numbers__div_remainder",
    "numbers__div_remainder_composed",
    "numbers__gcd",
    "numbers__gcd_composed",
    "numbers__is_factor",
    "numbers__is_factor_composed",
    "numbers__is_prime",
    "numbers__is_prime_composed",
    "numbers__lcm",
    "numbers__lcm_composed",
    "numbers__list_prime_factors",
    "numbers__list_prime_factors_composed",
    "numbers__place_value",
    "numbers__place_value_composed",
    "numbers__round_number",
    "numbers__round_number_composed",
    "polynomials__add",
    "polynomials__coefficient_named",
    "polynomials__collect",
    "polynomials__compose",
    "polynomials__evaluate",
    "polynomials__evaluate_composed",
    "polynomials__expand",
    "polynomials__simplify_power",
    "probability__swr_p_level_set",
    "probability__swr_p_sequence",
]

_QUESTION = "question"
_ANSWER = "answer"

_DATASET_VERSION = "mathematics_dataset-v1.0"


def _generate_builder_configs():
  """Generate configs with different subsets of mathematics dataset."""
  configs = []
  for module in sorted(set(_MODULES)):
    configs.append(
        tfds.core.BuilderConfig(
            name=module,
            version=tfds.core.Version("1.0.0"),
        )
    )

  return configs


class Builder(tfds.core.GeneratorBasedBuilder):
  """Math Dataset."""

  BUILDER_CONFIGS = _generate_builder_configs()

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            _QUESTION: tfds.features.Text(),
            _ANSWER: tfds.features.Text(),
        }),
        supervised_keys=(_QUESTION, _ANSWER),
        homepage="https://github.com/deepmind/mathematics_dataset",
    )

  def _read_data_from_all_categories(self, directory, config, categories):
    lines = []
    for category in categories:
      data_file = os.path.join(directory, _DATASET_VERSION, category, config)
      if tf.io.gfile.exists(data_file):
        with epath.Path(data_file).open() as f:
          ls = f.read().split("\n")

          for l in ls[::-1]:
            if not l:
              ls.remove(l)

          lines.extend(ls)

    return lines

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    directory = dl_manager.download_and_extract(_DATA_URL)
    config = self.builder_config.name + ".txt"

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "directory": directory,
                "config": config,
                "categories": _TRAIN_CATEGORY,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "directory": directory,
                "config": config,
                "categories": _INTERPOLATE_CATEGORY,
            },
        ),
    ]

  def _generate_examples(self, directory, config, categories):
    """Yields examples based on directory, module file.."""

    lines = self._read_data_from_all_categories(directory, config, categories)
    logging.info("%s: %s contains total: %d", categories, config, len(lines))
    questions = lines[::2]
    answers = lines[1::2]

    assert len(answers) == len(
        questions
    ), "answers: %d do not match questions: %d" % (len(answers), len(questions))

    for idx, (q, a) in enumerate(zip(questions, answers)):
      result = {_QUESTION: q, _ANSWER: a}
      if all(result.values()):
        yield idx, result
