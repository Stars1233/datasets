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

"""Tests for cycle_gan dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import cycle_gan


class CycleGANTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cycle_gan.CycleGAN
  BUILDER_CONFIG_NAMES_TO_TEST = ["horse2zebra"]
  SPLITS = {
      "trainA": 2,
      "testA": 2,
      "trainB": 2,
      "testB": 2,
  }


if __name__ == "__main__":
  testing.test_main()
