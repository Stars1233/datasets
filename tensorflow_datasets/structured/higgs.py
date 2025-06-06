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

"""HIGGS Data Set."""

from __future__ import annotations

import csv

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

# From https://arxiv.org/abs/1402.4735
_CITATION = """\
@article{Baldi:2014kfa,
      author         = "Baldi, Pierre and Sadowski, Peter and Whiteson, Daniel",
      title          = "{Searching for Exotic Particles in High-Energy Physics
                        with Deep Learning}",
      journal        = "Nature Commun.",
      volume         = "5",
      year           = "2014",
      pages          = "4308",
      doi            = "10.1038/ncomms5308",
      eprint         = "1402.4735",
      archivePrefix  = "arXiv",
      primaryClass   = "hep-ph",
      SLACcitation   = "%%CITATION = ARXIV:1402.4735;%%"
}
"""

_DESCRIPTION = """\
The data has been produced using Monte Carlo simulations.
The first 21 features (columns 2-22) are kinematic properties
measured by the particle detectors in the accelerator.
The last seven features are functions of the first 21 features;
these are high-level features derived by physicists to help
discriminate between the two classes. There is an interest
in using deep learning methods to obviate the need for physicists
to manually develop such features. Benchmark results using
Bayesian Decision Trees from a standard physics package and
5-layer neural networks are presented in the original paper.
"""

_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz'


class Higgs(tfds.core.GeneratorBasedBuilder):
  """HIGGS Data Set."""

  VERSION = tfds.core.Version('2.0.0')
  RELEASE_NOTES = {
      '2.0.0': 'New split API (https://tensorflow.org/datasets/splits)',
  }

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'class_label': np.float32,  # 1 for signal, 0 for background
            # 21 low-level features
            'lepton_pT': np.float64,
            'lepton_eta': np.float64,
            'lepton_phi': np.float64,
            'missing_energy_magnitude': np.float64,
            'missing_energy_phi': np.float64,
            'jet_1_pt': np.float64,
            'jet_1_eta': np.float64,
            'jet_1_phi': np.float64,
            'jet_1_b-tag': np.float64,
            'jet_2_pt': np.float64,
            'jet_2_eta': np.float64,
            'jet_2_phi': np.float64,
            'jet_2_b-tag': np.float64,
            'jet_3_pt': np.float64,
            'jet_3_eta': np.float64,
            'jet_3_phi': np.float64,
            'jet_3_b-tag': np.float64,
            'jet_4_pt': np.float64,
            'jet_4_eta': np.float64,
            'jet_4_phi': np.float64,
            'jet_4_b-tag': np.float64,
            # 7 high-level features
            'm_jj': np.float64,
            'm_jjj': np.float64,
            'm_lv': np.float64,
            'm_jlv': np.float64,
            'm_bb': np.float64,
            'm_wbb': np.float64,
            'm_wwbb': np.float64,
        }),
        supervised_keys=None,
        homepage='https://archive.ics.uci.edu/ml/datasets/HIGGS',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'file_path': path,
            },
        ),
    ]

  def _generate_examples(self, file_path):
    """Generate features given the directory path.

    Args:
      file_path: path where the csv file is stored

    Yields:
      The features, per row.
    """

    fieldnames = [
        'class_label',
        'lepton_pT',
        'lepton_eta',
        'lepton_phi',
        'missing_energy_magnitude',
        'missing_energy_phi',
        'jet_1_pt',
        'jet_1_eta',
        'jet_1_phi',
        'jet_1_b-tag',
        'jet_2_pt',
        'jet_2_eta',
        'jet_2_phi',
        'jet_2_b-tag',
        'jet_3_pt',
        'jet_3_eta',
        'jet_3_phi',
        'jet_3_b-tag',
        'jet_4_pt',
        'jet_4_eta',
        'jet_4_phi',
        'jet_4_b-tag',
        'm_jj',
        'm_jjj',
        'm_lv',
        'm_jlv',
        'm_bb',
        'm_wbb',
        'm_wwbb',
    ]

    with epath.Path(file_path).open() as csvfile:
      reader = csv.DictReader(csvfile, fieldnames=fieldnames)
      for i, row in enumerate(reader):
        yield i, row
