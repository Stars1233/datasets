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

"""hellaswag dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import hellaswag


class HellaswagTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = hellaswag.Hellaswag
  SPLITS = {
      'train': 2,
      'validation': 4,
      'test': 4,
      'train_activitynet': 1,
      'train_wikihow': 1,
      'validation_ind_activitynet': 1,
      'validation_ood_activitynet': 1,
      'test_ind_activitynet': 1,
      'test_ood_activitynet': 1,
      'validation_ind_wikihow': 1,
      'validation_ood_wikihow': 1,
      'test_ind_wikihow': 1,
      'test_ood_wikihow': 1,
  }
  DL_EXTRACT_RESULT = {
      'train': 'hellaswag_train.jsonl',
      'test': 'hellaswag_test.jsonl',
      'validation': 'hellaswag_val.jsonl',
  }
  OVERLAPPING_SPLITS = [
      'train_activitynet',
      'train_wikihow',
      'validation_ind_activitynet',
      'validation_ood_activitynet',
      'test_ind_activitynet',
      'test_ood_activitynet',
      'validation_ind_wikihow',
      'validation_ood_wikihow',
      'test_ind_wikihow',
      'test_ood_wikihow',
  ]


if __name__ == '__main__':
  tfds.testing.test_main()
