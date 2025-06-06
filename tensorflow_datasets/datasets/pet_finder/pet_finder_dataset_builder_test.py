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

"""Test for PetFinder."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.pet_finder import pet_finder_dataset_builder


class PetFinderTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = pet_finder_dataset_builder.Builder
  SPLITS = {
      'train': 2,  # Number of fake train example
      'test': 2,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = {
      'train': 'train.csv',
      'train_images': 'train_images',
      'test': 'test.csv',
      'test_images': 'test_images',
  }


if __name__ == '__main__':
  testing.test_main()
