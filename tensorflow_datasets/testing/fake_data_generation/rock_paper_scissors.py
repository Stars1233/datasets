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

r"""Generate fake data for rock_paper_scissors dataset.

"""

import os
import zipfile

from absl import app
from absl import flags
from tensorflow_datasets.core import utils
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string(
    'tfds_dir',
    os.fspath(utils.tfds_write_path()),
    'Path to tensorflow_datasets directory',
)

FLAGS = flags.FLAGS


def _output_dir():
  return os.path.join(
      FLAGS.tfds_dir,
      'testing',
      'test_data',
      'fake_examples',
      'rock_paper_scissors',
  )


def create_zip(fname, prefix):
  out_path = os.path.join(_output_dir(), fname)
  png = fake_data_utils.get_random_png(height=1, width=1)
  with zipfile.ZipFile(out_path, 'w') as myzip:
    myzip.write(png, prefix + 'rock/0.png')
    myzip.write(png, prefix + 'paper/0.png')
    myzip.write(png, prefix + 'scissors/0.png')


def main(argv):
  del argv
  create_zip('rps_train.zip', 'rps/')
  create_zip('rps_test.zip', 'rps-test-set/')


if __name__ == '__main__':
  app.run(main)
