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

"""OpinionAbstracts Dataset Test."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.opinion_abstracts import opinion_abstracts_dataset_builder


class OpinionAbstractsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = opinion_abstracts_dataset_builder.Builder
  SPLITS = {
      "train": 1,
  }


if __name__ == "__main__":
  testing.test_main()
