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

"""GCS utils test."""

from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import gcs_utils
from tensorflow_datasets.testing import test_utils

import os
import tempfile
import tensorflow_datasets as tfds
class GcsUtilsTest(testing.TestCase):
  DO_NOT_APPLY_FIXTURES = [test_utils.disable_gcs_access]
  def test_is_dataset_accessible(self):
    gcs_utils._is_gcs_disabled = False
    self.assertTrue(gcs_utils.is_dataset_on_gcs('mnist/1.0.0'))
    self.assertFalse(gcs_utils.is_dataset_on_gcs('non_dataset/1.0.0'))
    gcs_utils._is_gcs_disabled = True
  def test_download_dataset(self):
    gcs_utils._is_gcs_disabled = False
    files = [
        'gs://tfds-data/dataset_info/mnist/2.0.0/dataset_info.json',
        'gs://tfds-data/dataset_info/mnist/2.0.0/image.image.json',
    ]
    self.assertCountEqual(
        gcs_utils.gcs_dataset_info_files('mnist/2.0.0'),
        [tfds.core.as_path(f) for f in files],
    )
    with tempfile.TemporaryDirectory() as tmp_dir:
      gcs_utils.download_gcs_dataset(
          dataset_name='mnist/2.0.0', local_dataset_dir=tmp_dir
      )
      self.assertCountEqual(
          os.listdir(tmp_dir),
          [
              'mnist-test.tfrecord-00000-of-00001',
              'mnist-train.tfrecord-00000-of-00001',
              'dataset_info.json',
              'image.image.json',
          ],
      )
    gcs_utils._is_gcs_disabled = True
  def test_mnist(self):
    mnist = tfds.image_classification.MNIST(
        data_dir=gcs_utils.gcs_path('datasets')
    )
    ds = tfds.as_numpy(mnist.as_dataset(split='train').take(1))
    example = next(iter(ds))
    _ = example['image'], example['label']


class GcsUtilsDisabledTest(testing.TestCase):

  DO_NOT_APPLY_FIXTURES = [test_utils.disable_gcs_access]

  def test_is_dataset_accessible(self):
    is_ds_on_gcs = gcs_utils.is_dataset_on_gcs('mnist/1.0.0')
    self.assertFalse(is_ds_on_gcs)


if __name__ == '__main__':
  testing.test_main()
