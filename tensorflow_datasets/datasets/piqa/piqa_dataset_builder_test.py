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

"""Tests for PIQA dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.piqa import piqa_dataset_builder


class PiqaTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = piqa_dataset_builder.Builder

  SPLITS = {
      "train": 2,  # Number of fake train example.
      "validation": 2,  # Number of fake validation example.
  }


if __name__ == "__main__":
  testing.test_main()
