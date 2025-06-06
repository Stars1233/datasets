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

"""conll2003 dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.conll2003 import conll2003


class Conll2003Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for conll2003 dataset."""

  DATASET_CLASS = conll2003.Conll2003
  SPLITS = {
      'train': 3,
      'dev': 1,
      'test': 1,
  }


if __name__ == '__main__':
  tfds.testing.test_main()
