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

"""Image datasets."""

from tensorflow_datasets.image.abstract_reasoning import AbstractReasoning
from tensorflow_datasets.image.aflw2k3d import Aflw2k3d
from tensorflow_datasets.image.arc import ARC
from tensorflow_datasets.image.bccd import BCCD
from tensorflow_datasets.image.binarized_mnist import BinarizedMNIST
from tensorflow_datasets.image.celeba import CelebA
from tensorflow_datasets.image.celebahq import CelebAHq
from tensorflow_datasets.image.cityscapes import Cityscapes
from tensorflow_datasets.image.clevr import CLEVR
from tensorflow_datasets.image.clic import CLIC
from tensorflow_datasets.image.coil100 import Coil100
from tensorflow_datasets.image.div2k import Div2k
from tensorflow_datasets.image.downsampled_imagenet import DownsampledImagenet
from tensorflow_datasets.image.dsprites import Dsprites
from tensorflow_datasets.image.duke_ultrasound import DukeUltrasound
from tensorflow_datasets.image.flic import Flic
from tensorflow_datasets.image.lost_and_found import LostAndFound
from tensorflow_datasets.image.lsun import Lsun
from tensorflow_datasets.image.nyu_depth_v2 import NyuDepthV2
from tensorflow_datasets.image.pass_dataset import PASS
from tensorflow_datasets.image.s3o4d import S3o4d
from tensorflow_datasets.image.scene_parse_150 import SceneParse150
from tensorflow_datasets.image.shapes3d import Shapes3d
from tensorflow_datasets.image.symmetric_solids import SymmetricSolids
from tensorflow_datasets.image.the300w_lp import The300wLp
from tensorflow_datasets.image_classification.beans import Beans
from tensorflow_datasets.image_classification.bigearthnet import Bigearthnet
from tensorflow_datasets.image_classification.binary_alpha_digits import BinaryAlphaDigits
from tensorflow_datasets.image_classification.caltech import Caltech101
from tensorflow_datasets.image_classification.caltech_birds import CaltechBirds2010
from tensorflow_datasets.image_classification.cars196 import Cars196
from tensorflow_datasets.image_classification.cassava import Cassava
from tensorflow_datasets.image_classification.cats_vs_dogs import CatsVsDogs
from tensorflow_datasets.image_classification.cbis_ddsm import CuratedBreastImagingDDSM
from tensorflow_datasets.image_classification.chexpert import Chexpert
from tensorflow_datasets.image_classification.cifar import Cifar10
from tensorflow_datasets.image_classification.cifar import Cifar100
from tensorflow_datasets.image_classification.cifar10_1 import Cifar10_1
from tensorflow_datasets.image_classification.cifar10_corrupted import Cifar10Corrupted
from tensorflow_datasets.image_classification.citrus import CitrusLeaves
from tensorflow_datasets.image_classification.cmaterdb import Cmaterdb
from tensorflow_datasets.image_classification.colorectal_histology import ColorectalHistology
from tensorflow_datasets.image_classification.colorectal_histology import ColorectalHistologyLarge
from tensorflow_datasets.image_classification.cycle_gan import CycleGAN
from tensorflow_datasets.image_classification.deep_weeds import DeepWeeds
from tensorflow_datasets.image_classification.diabetic_retinopathy_detection import DiabeticRetinopathyDetection
from tensorflow_datasets.image_classification.dmlab import Dmlab
from tensorflow_datasets.image_classification.dtd import Dtd
from tensorflow_datasets.image_classification.eurosat import Eurosat
from tensorflow_datasets.image_classification.flowers import TFFlowers
from tensorflow_datasets.image_classification.food101 import Food101
from tensorflow_datasets.image_classification.geirhos_conflict_stimuli import GeirhosConflictStimuli
from tensorflow_datasets.image_classification.horses_or_humans import HorsesOrHumans
from tensorflow_datasets.image_classification.imagenet import Imagenet2012
from tensorflow_datasets.image_classification.imagenet2012_corrupted import Imagenet2012Corrupted
from tensorflow_datasets.image_classification.imagenet2012_subset import Imagenet2012Subset
from tensorflow_datasets.image_classification.imagenet_resized import ImagenetResized
from tensorflow_datasets.image_classification.imagenette import Imagenette
from tensorflow_datasets.image_classification.imagewang import Imagewang
from tensorflow_datasets.image_classification.inaturalist import INaturalist2017
from tensorflow_datasets.image_classification.lfw import LFW
from tensorflow_datasets.image_classification.malaria import Malaria
from tensorflow_datasets.image_classification.mnist import EMNIST
from tensorflow_datasets.image_classification.mnist import FashionMNIST
from tensorflow_datasets.image_classification.mnist import KMNIST
from tensorflow_datasets.image_classification.mnist import MNIST
from tensorflow_datasets.image_classification.mnist_corrupted import MNISTCorrupted
from tensorflow_datasets.image_classification.omniglot import Omniglot
from tensorflow_datasets.image_classification.oxford_flowers102 import OxfordFlowers102
from tensorflow_datasets.image_classification.oxford_iiit_pet import OxfordIIITPet
from tensorflow_datasets.image_classification.patch_camelyon import PatchCamelyon
from tensorflow_datasets.image_classification.pet_finder import PetFinder
from tensorflow_datasets.image_classification.places365_small import Places365Small
from tensorflow_datasets.image_classification.plant_leaves import PlantLeaves
from tensorflow_datasets.image_classification.plant_village import PlantVillage
from tensorflow_datasets.image_classification.plantae_k import PlantaeK
from tensorflow_datasets.image_classification.quickdraw import QuickdrawBitmap
from tensorflow_datasets.image_classification.resisc45 import Resisc45
from tensorflow_datasets.image_classification.rock_paper_scissors import RockPaperScissors
from tensorflow_datasets.image_classification.smallnorb import Smallnorb
from tensorflow_datasets.image_classification.so2sat import So2sat
from tensorflow_datasets.image_classification.stanford_dogs import StanfordDogs
from tensorflow_datasets.image_classification.stanford_online_products import StanfordOnlineProducts
from tensorflow_datasets.image_classification.sun import Sun397
from tensorflow_datasets.image_classification.svhn import SvhnCropped
from tensorflow_datasets.image_classification.uc_merced import UcMerced
from tensorflow_datasets.image_classification.visual_domain_decathlon import VisualDomainDecathlon
