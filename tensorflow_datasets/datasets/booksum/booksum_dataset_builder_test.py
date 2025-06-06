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

"""summscreen dataset."""
from tensorflow_datasets.datasets.booksum import booksum_dataset_builder
import tensorflow_datasets.public_api as tfds


class BooksumTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for booksum dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = ["book", "chapter"]

  DATASET_CLASS = booksum_dataset_builder.Builder
  SPLITS = {
      "train": 1,  # Number of fake train example
      "validation": 1,  # Number of fake train example
      "test": 1,  # Number of fake train example
  }


if __name__ == "__main__":
  tfds.testing.test_main()
