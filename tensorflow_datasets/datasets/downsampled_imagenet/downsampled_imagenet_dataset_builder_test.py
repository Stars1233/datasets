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

"""Tests for downsampled_imagenet dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.downsampled_imagenet import downsampled_imagenet_dataset_builder
import tensorflow_datasets.public_api as tfds


class DownsampledImagenetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = downsampled_imagenet_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ["32x32", "64x64"]

  SPLITS = {
      tfds.Split.TRAIN: 2,
      tfds.Split.VALIDATION: 2,
  }

  DL_EXTRACT_RESULT = [
      "train_32x32.tar",
      "valid_32x32.tar",
  ]


if __name__ == "__main__":
  testing.test_main()
