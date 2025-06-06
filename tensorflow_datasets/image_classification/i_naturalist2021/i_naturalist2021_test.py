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

"""i_naturalist2021 dataset."""

from tensorflow_datasets.image_classification.i_naturalist2021 import i_naturalist2021
import tensorflow_datasets.public_api as tfds


class INaturalist2021Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for i_naturalist2021 dataset."""

  DATASET_CLASS = i_naturalist2021.INaturalist2021
  SPLITS = {
      "mini": 2,  # Number of fake mini examples
      "test": 3,  # Number of fake test examples
      "train": 3,  # Number of fake train examples
      "val": 2,  # Number of fake val examples
  }
  OVERLAPPING_SPLITS = ["mini", "train"]

  DL_EXTRACT_RESULT = {}
  for split, split_file in i_naturalist2021._SPLIT_FILENAMES.items():
    DL_EXTRACT_RESULT[f"{split}_img"] = f"{split_file}.tar.gz"
    DL_EXTRACT_RESULT[f"{split}_json"] = split_file

  SKIP_CHECKSUMS = True


if __name__ == "__main__":
  tfds.testing.test_main()
