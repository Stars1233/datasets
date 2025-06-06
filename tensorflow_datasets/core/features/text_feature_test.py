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

# coding=utf-8
"""Tests for tensorflow_datasets.core.deprecated.text_feature."""

import numpy as np
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import features
from tensorflow_datasets.core.deprecated.text import text_encoder


class TextFeatureTest(testing.FeatureExpectationsTestCase):

  def test_text(self):
    nonunicode_text = 'hello world'
    unicode_text = '你好'

    self.assertFeature(
        feature=features.Text(),
        shape=(),
        dtype=np.str_,
        tests=[
            # Non-unicode
            testing.FeatureExpectationItem(
                value=nonunicode_text,
                expected=b'hello world',
                expected_np=b'hello world',
            ),
            # Unicode
            testing.FeatureExpectationItem(
                value=unicode_text,
                expected=b'\xe4\xbd\xa0\xe5\xa5\xbd',  # 你好 in bytes
                expected_np=b'\xe4\xbd\xa0\xe5\xa5\xbd',  # 你好 in bytes
            ),
            # Empty string
            testing.FeatureExpectationItem(
                value='',
                expected=b'',
                expected_np=b'',
            ),
        ],
    )

  def test_text_encoded(self):
    unicode_text = '你好'

    # Unicode integer-encoded by byte
    self.assertFeature(
        feature=features.Text(encoder=text_encoder.ByteTextEncoder()),
        shape=(None,),
        dtype=np.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=unicode_text,
                expected=[i + 1 for i in [228, 189, 160, 229, 165, 189]],
            ),
            # Empty string
            testing.FeatureExpectationItem(
                value='',
                expected=[],
            ),
        ],
        skip_feature_tests=True,
    )

  def test_text_conversion(self):
    text_f = features.Text(encoder=text_encoder.ByteTextEncoder())
    text = '你好'
    self.assertEqual(text, text_f.ints2str(text_f.str2ints(text)))

  def test_save_load_metadata(self):
    encoder = text_encoder.ByteTextEncoder(additional_tokens=['HI'])
    text_f = features.Text(encoder=encoder)
    text = 'HI 你好'
    ids = text_f.str2ints(text)
    self.assertEqual(1, ids[0])

    with testing.tmp_dir(self.get_temp_dir()) as data_dir:
      feature_name = 'dummy'
      text_f.save_metadata(data_dir, feature_name)

      # Test loading it from a newly instantiated feature.
      new_f = features.Text(encoder=encoder)
      new_f.load_metadata(data_dir, feature_name)
      self.assertEqual(ids, new_f.str2ints(text))

      # Test that loading it without an encoder results in an error.
      with pytest.raises(
          ValueError, match='Text feature files found for feature.+'
      ):
        new_f_no_encoder = features.Text()
        new_f_no_encoder.load_metadata(data_dir, feature_name)


if __name__ == '__main__':
  testing.test_main()
