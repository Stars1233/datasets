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

"""Imagenet LT datasets."""

import io
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

_TRAIN_SUBSET = (
    'https://drive.google.com/uc?export=download&'
    'id=1Sl1cwy6Dei1I1BMS1YKjI35fkaR1UA_7'
)

_VAL_SUBSET = (
    'https://drive.google.com/uc?export=download&'
    'id=1AjYczW4khrQrwPIygXUkHF-Qv4QGEsCF'
)


class Builder(tfds.core.GeneratorBasedBuilder):
  """Long-tailed version of the ImageNet2012 dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain two files: ILSVRC2012_img_train.tar and
  ILSVRC2012_img_val.tar.
  You need to register on http://www.image-net.org/download-images in order
  to get the link to download the dataset.
  """

  def _info(self):
    """Define the dataset info."""
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
        }),
        supervised_keys=('image', 'label'),
        homepage='https://github.com/zhmiao/OpenLongTailRecognition-OLTR',
    )

  def _postprocess_subset_list(self, subset):
    """Postprocess the subset list."""

    # The original subset contains lines such as
    # "train/n01440764/n01440764_190.JPEG 0".
    # Postprocessing removes the redundant info and only keeps the image name,
    # i.e. n01440764_190.JPEG.
    post_subset = [
        os.path.basename(cur_item.split(' ')[0]) for cur_item in subset
    ]
    return post_subset

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')

    # We don't import the original test split, as it doesn't include labels.
    # These were never publicly released.
    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet-LT requires manual download of the ImageNet2012 data. '
          'Please download the train and val set and place them into:'
          '{}, {}'.format(train_path, val_path)
      )

    # Download and load subset file.
    downloaded_dirs = dl_manager.download({
        'train': _TRAIN_SUBSET,
        'validation': _VAL_SUBSET,
    })

    with tf.io.gfile.GFile(downloaded_dirs['train']) as fp:
      train_subset = fp.read().splitlines()
    train_subset = self._postprocess_subset_list(train_subset)

    with tf.io.gfile.GFile(downloaded_dirs['validation']) as fp:
      val_subset = fp.read().splitlines()
    val_subset = self._postprocess_subset_list(val_subset)

    return {
        'train': self._generate_examples(
            archive=dl_manager.iter_archive(train_path), subset=train_subset
        ),
        'validation': self._generate_examples(
            archive=dl_manager.iter_archive(train_path), subset=val_subset
        ),
        'test': self._generate_examples(
            archive=dl_manager.iter_archive(val_path),
            validation_labels=imagenet_common.get_validation_labels(val_path),
        ),
    }

  def _generate_examples(self, archive, subset=None, validation_labels=None):
    """Yields examples."""
    # Test split in ImageNet-LT is the validation split in the original ImageNet
    if validation_labels:
      for key, example in imagenet_common.generate_examples_validation(
          archive, validation_labels
      ):
        yield key, example

    # Training and validation split. Main archive contains archives names after
    # a synset noun.
    # Each sub-archive contains pictures associated to that synset.
    for fname, fobj in archive:
      label = fname[:-4]  # fname is something like 'n01632458.tar'
      # TODO(b/117643231): in py3, the following lines trigger tarfile module
      # to call `fobj.seekable()`, which Gfile doesn't have. We should find an
      # alternative, as this loads ~150MB in RAM.
      fobj_mem = io.BytesIO(fobj.read())
      for image_fname, image in tfds.download.iter_archive(
          fobj_mem, tfds.download.ExtractMethod.TAR_STREAM
      ):  # pytype: disable=wrong-arg-types  # gen-stub-imports
        if subset is None or image_fname in subset:  # filtering using subset.
          record = {
              'file_name': image_fname,
              'image': image,
              'label': label,
          }
          yield image_fname, record
