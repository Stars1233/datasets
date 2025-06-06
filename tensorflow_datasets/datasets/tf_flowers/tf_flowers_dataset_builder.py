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

"""Flowers dataset."""

import os

import tensorflow_datasets.public_api as tfds

_URL = "http://download.tensorflow.org/example_images/flower_photos.tgz"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Flowers dataset."""

  VERSION = tfds.core.Version("3.0.1")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(
                names=["dandelion", "daisy", "tulips", "sunflowers", "roses"]
            ),
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.tensorflow.org/tutorials/load_data/images",
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"images_dir_path": dl_manager.iter_archive(path)},
        ),
    ]

  def _generate_examples(self, images_dir_path):
    """Generate flower images and labels given the image directory path.

    Args:
      images_dir_path: path to the directory where the images are stored.

    Yields:
      The image path and its corresponding label.
    """
    for fname, fobj in images_dir_path:
      if fname.endswith(".jpg"):
        image_dir, image_file = os.path.split(fname)
        d = os.path.basename(image_dir)
        record = {"image": fobj, "label": d.lower()}
        yield "%s/%s" % (d, image_file), record
