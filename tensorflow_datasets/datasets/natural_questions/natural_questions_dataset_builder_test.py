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

"""Tests for natural_questions dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.natural_questions import natural_questions_dataset_builder


class NaturalQuestionsTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["default"]
  DATASET_CLASS = natural_questions_dataset_builder.Builder
  SPLITS = {
      "train": 3,
      "validation": 2,
  }

  DL_EXTRACT_RESULT = {
      "train": ["nq-train-00.jsonl.gz", "nq-train-01.jsonl.gz"],
      "validation": ["nq-dev-00.jsonl.gz"],
  }


if __name__ == "__main__":
  testing.test_main()
