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

"""Dataset definition for story_cloze.

DEPRECATED!
If you want to use the StoryCloze dataset builder class, use:
tfds.builder_cls('story_cloze')
"""

from tensorflow_datasets.core import lazy_builder_import

StoryCloze = lazy_builder_import.LazyBuilderImport('story_cloze')
