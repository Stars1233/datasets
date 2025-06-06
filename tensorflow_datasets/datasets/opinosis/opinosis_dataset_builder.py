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

"""Opinosis Opinion Dataset."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://github.com/kavgan/opinosis-summarization/raw/master/OpinosisDataset1.0_0.zip"

_REVIEW_SENTS = "review_sents"
_SUMMARIES = "summaries"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Opinosis Opinion Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            _REVIEW_SENTS: tfds.features.Text(),
            _SUMMARIES: tfds.features.Sequence(tfds.features.Text()),
        }),
        supervised_keys=(_REVIEW_SENTS, _SUMMARIES),
        homepage="http://kavita-ganesan.com/opinosis/",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extract_path = dl_manager.download_and_extract(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": extract_path},
        ),
    ]

  def _generate_examples(self, path=None):
    """Yields examples."""
    topics_path = os.path.join(path, "topics")
    filenames = tf.io.gfile.listdir(topics_path)
    for filename in filenames:
      file_path = os.path.join(topics_path, filename)
      topic_name = filename.split(".txt")[0]
      with tf.io.gfile.GFile(file_path, "rb") as src_f:
        input_data = src_f.read()
      summaries_path = os.path.join(path, "summaries-gold", topic_name)
      summary_lst = []
      for summ_filename in sorted(tf.io.gfile.listdir(summaries_path)):
        file_path = os.path.join(summaries_path, summ_filename)
        with tf.io.gfile.GFile(file_path, "rb") as tgt_f:
          data = tgt_f.read().strip()
          summary_lst.append(data)
      summary_data = summary_lst
      yield filename, {_REVIEW_SENTS: input_data, _SUMMARIES: summary_data}
