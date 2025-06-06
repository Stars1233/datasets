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

"""Test for XSum dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.summarization import xsum


class XsumTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = xsum.Xsum
  SPLITS = {
      "train": 1,  # Number of fake train example
      "validation": 1,  # Number of fake validation example
      "test": 1,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = "XSum-TRAINING-DEV-TEST-SPLIT-90-5-5.json"


if __name__ == "__main__":
  testing.test_main()
