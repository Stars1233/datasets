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

"""SpeechCommands dataset."""

import os

import numpy as np
from tensorflow_datasets.core import lazy_imports_lib
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_PATH = (
    'http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz'
)
_TEST_DOWNLOAD_PATH_ = (
    'http://download.tensorflow.org/data/speech_commands_test_set_v0.02.tar.gz'
)

_SPLITS = ['train', 'valid', 'test']

WORDS = ['down', 'go', 'left', 'no', 'off', 'on', 'right', 'stop', 'up', 'yes']
SILENCE = '_silence_'
UNKNOWN = '_unknown_'
BACKGROUND_NOISE = '_background_noise_'
SAMPLE_RATE = 16000


class Builder(tfds.core.GeneratorBasedBuilder):
  """The Speech Commands dataset for keyword detection."""

  VERSION = tfds.core.Version('0.0.3')
  RELEASE_NOTES = {
      '0.0.3': 'Fix audio data type with dtype=tf.int16.',
  }

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(
                file_format='wav', sample_rate=SAMPLE_RATE, dtype=np.int16
            ),
            'label': tfds.features.ClassLabel(names=WORDS + [SILENCE, UNKNOWN]),
        }),
        supervised_keys=('audio', 'label'),
        # Homepage of the dataset for documentation
        homepage='https://arxiv.org/abs/1804.03209',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    dl_path, dl_test_path = dl_manager.download(
        [_DOWNLOAD_PATH, _TEST_DOWNLOAD_PATH_]
    )

    train_paths, validation_paths = self._split_archive(
        dl_manager.iter_archive(dl_path)
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'archive': dl_manager.iter_archive(dl_path),
                'file_list': train_paths,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'archive': dl_manager.iter_archive(dl_path),
                'file_list': validation_paths,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'archive': dl_manager.iter_archive(dl_test_path),
                'file_list': None,
            },
        ),
    ]

  def _generate_examples(self, archive, file_list):
    """Yields examples."""
    for path, file_obj in archive:
      if file_list is not None and path not in file_list:
        continue
      relpath, wavname = os.path.split(path)
      _, word = os.path.split(relpath)
      example_id = '{}_{}'.format(word, wavname)
      if word in WORDS:
        label = word
      elif word == SILENCE or word == BACKGROUND_NOISE:
        # The main tar file already contains all of the test files, except for
        # the silence ones. In fact it does not contain silence files at all.
        # So for the test set we take the silence files from the test tar file,
        # while for train and validation we build them from the
        # _background_noise_ folder.
        label = SILENCE
      else:
        # Note that in the train and validation there are a lot more _unknown_
        # labels than any of the other ones.
        label = UNKNOWN

      if word == BACKGROUND_NOISE:
        # Special handling of background noise. We need to cut these files to
        # many small files with 1 seconds length, and transform it to silence.
        audio_samples = np.array(
            lazy_imports_lib.lazy_imports.pydub.AudioSegment.from_file(
                file_obj, format='wav'
            ).get_array_of_samples()
        )

        for start in range(
            0, len(audio_samples) - SAMPLE_RATE, SAMPLE_RATE // 2
        ):
          audio_segment = audio_samples[start : start + SAMPLE_RATE]
          cur_id = '{}_{}'.format(example_id, start)
          example = {'audio': audio_segment, 'label': label}
          yield cur_id, example
      else:
        try:
          example = {
              'audio': np.array(
                  lazy_imports_lib.lazy_imports.pydub.AudioSegment.from_file(
                      file_obj, format='wav'
                  ).get_array_of_samples()
              ),
              'label': label,
          }
          yield example_id, example
        except (
            lazy_imports_lib.lazy_imports.pydub.exceptions.CouldntDecodeError
        ):
          pass

  def _split_archive(self, train_archive):
    train_paths = []
    for path, file_obj in train_archive:
      if 'testing_list.txt' in path:
        train_test_paths = file_obj.read().strip().splitlines()
        train_test_paths = [p.decode('ascii') for p in train_test_paths]
      elif 'validation_list.txt' in path:
        validation_paths = file_obj.read().strip().splitlines()
        validation_paths = [p.decode('ascii') for p in validation_paths]
      elif path.endswith('.wav'):
        train_paths.append(path)

    # Original validation files did include silence - we add them manually here
    validation_paths.append(os.path.join(BACKGROUND_NOISE, 'running_tap.wav'))

    # The paths for the train set is just whichever paths that do not exist in
    # either the test or validation splits.
    train_paths = (
        set(train_paths) - set(validation_paths) - set(train_test_paths)
    )

    return train_paths, validation_paths
