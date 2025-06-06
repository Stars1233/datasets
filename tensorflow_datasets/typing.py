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

"""TFDS typing annotations."""

from etils import epath
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import splits
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.utils import type_utils

# pylint: disable=unused-import
from tensorflow_datasets.core.utils.type_utils import *  # pylint: disable=wildcard-import
# pylint: enable=unused-import

# Accept both `str` and `pathlib.Path`-like
PathLike = epath.PathLike

DecoderArg = decode.partial_decode.DecoderArg
FeatureSpecs = decode.partial_decode.FeatureSpecs
FeatureConnectorArg = feature.FeatureConnectorArg
SplitArg = splits.SplitArg

__all__ = type_utils.__all__ + [
    'DecoderArg',
    'FeatureConnectorArg',
    'FeatureSpecs',
    'PathLike',
    'SplitArg',
]
