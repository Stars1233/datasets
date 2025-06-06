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

"""Tests for salient_span_wikipedia dataset module."""
from tensorflow_datasets import testing
from tensorflow_datasets.datasets.salient_span_wikipedia import salient_span_wikipedia_dataset_builder


class SalientSpanWikipediaSentencesTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = salient_span_wikipedia_dataset_builder.Builder

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    salient_span_wikipedia_dataset_builder._INPUT_FILE_PATTERN = str(
        cls.dummy_data / 'test_examples.tfrecord.gz'
    )

  BUILDER_CONFIG_NAMES_TO_TEST = ['sentences']
  SPLITS = {'train': 4}


class SalientSpanWikipediaDocumentsTest(SalientSpanWikipediaSentencesTest):
  BUILDER_CONFIG_NAMES_TO_TEST = ['documents']
  SPLITS = {'train': 2}


if __name__ == '__main__':
  testing.test_main()
