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

"""QA4MRE (CLEF 2011/2012/2013): a reading comprehension dataset."""

import os
import xml.etree.ElementTree as ET

from absl import logging
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# pylint: disable=anomalous-backslash-in-string

_BASE_URL = 'http://nlp.uned.es/clef-qa/repository/js/scripts/downloadFile.php?file=/var/www/html/nlp/clef-qa/repository/resources/QA4MRE/'

PATHS = {
    '2011': {
        '_TRACKS': 'main',
        '_PATH_TMPL_MAIN_GS': (
            '2011/Training_Data/Goldstandard/QA4MRE-2011-{}_GS.xml'
        ),
        '_LANGUAGES_MAIN': ('DE', 'EN', 'ES', 'IT', 'RO'),
    },
    '2012': {
        '_TRACKS': ('main', 'alzheimers'),
        '_PATH_TMPL_MAIN_GS': '2012/Main_Task/Training_Data/Goldstandard/Used_in_Evaluation/QA4MRE-2012-{}_GS.xml',
        '_LANGUAGES_MAIN': ('AR', 'BG', 'DE', 'EN', 'ES', 'IT', 'RO'),
        '_PATH_ALZHEIMER': '2012/Pilot_Tasks/Biomedical_About_Alzheimer/Training_Data/Goldstandard/QA4MRE-2012_BIOMEDICAL_GS.xml',
    },
    '2013': {
        '_TRACKS': ('main', 'alzheimers', 'entrance_exam'),
        '_PATH_TMPL_MAIN_GS': (
            '2013/Main_Task/Training_Data/Goldstandard/QA4MRE-2013-{}_GS.xml'
        ),
        '_LANGUAGES_MAIN': ('AR', 'BG', 'EN', 'ES', 'RO'),
        '_PATH_ALZHEIMER': '2013/Biomedical_About_Alzheimer/Training_Data/Goldstandard/QA4MRE-2013_BIO_GS-RUN.xml',
        '_PATH_ENTRANCE_EXAM': '2013/Entrance_Exams/Training_Data/Goldstandard/qa4mre-exam-test-withanswer.xml',
    },
}


def _get_question(
    topic_id, topic_name, test_id, document_id, document_str, question
):
  """Gets instance ID and features for every question.

  Args:
    topic_id: string
    topic_name: string
    test_id: string
    document_id: string
    document_str: string
    question: XML element for question

  Returns:
    id_: string. Unique ID for instance.
    feats: dict of instance features
  """

  question_id = question.attrib['q_id']
  for q_text in question.iter('q_str'):
    question_str = q_text.text
  possible_answers = list()
  for answer in question.iter('answer'):
    answer_id = answer.attrib['a_id']
    answer_str = answer.text
    possible_answers.append({'answer_id': answer_id, 'answer_str': answer_str})
    if 'correct' in answer.attrib:
      correct_answer_id = answer_id
      correct_answer_str = answer_str

  id_ = '_'.join([topic_id, topic_name, test_id, question_id])
  logging.info('ID: %s', id_)

  feats = {
      'topic_id': topic_id,
      'topic_name': topic_name,
      'test_id': test_id,
      'document_id': document_id,
      'document_str': document_str,
      'question_id': question_id,
      'question_str': question_str,
      'answer_options': possible_answers,
      'correct_answer_id': correct_answer_id,
      'correct_answer_str': correct_answer_str,
  }

  return id_, feats


class Qa4mreConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Qa4mre."""

  def __init__(self, *, year, track='main', language='EN', **kwargs):
    """BuilderConfig for Qa4Mre.

    Args:
      year: string, year of dataset
      track: string, the task track from PATHS[year]['_TRACKS'].
      language: string, Acronym for language in the main task.
      **kwargs: keyword arguments forwarded to super.
    """
    if track.lower() not in PATHS[year]['_TRACKS']:
      raise ValueError(
          'Incorrect track. Track should be one of the following: ',
          PATHS[year]['_TRACKS'],
      )

    if track.lower() != 'main' and language.upper() != 'EN':
      logging.warning(
          'Only English documents available for pilot '
          'tracks. Setting English by default.'
      )
      language = 'EN'

    if (
        track.lower() == 'main'
        and language.upper() not in PATHS[year]['_LANGUAGES_MAIN']
    ):
      raise ValueError(
          'Incorrect language for the main track. Correct options: ',
          PATHS[year]['_LANGUAGES_MAIN'],
      )

    self.year = year
    self.track = track.lower()
    self.lang = language.upper()

    name = self.year + '.' + self.track + '.' + self.lang

    description = (
        'This configuration includes the {} track for {} language in {} year.'
    ).format(self.track, self.lang, self.year)

    super(Qa4mreConfig, self).__init__(
        name=name,
        description=description,
        version=tfds.core.Version('0.1.0'),
        **kwargs,
    )


class Builder(tfds.core.GeneratorBasedBuilder):
  """QA4MRE dataset from CLEF shared tasks 2011, 2012, 2013."""

  BUILDER_CONFIGS = [
      Qa4mreConfig(
          year='2011', track='main', language='DE'
      ),  # 2011 Main track German (2011.main.DE)
      Qa4mreConfig(
          year='2011', track='main', language='EN'
      ),  # 2011 Main track English (2011.main.EN)
      Qa4mreConfig(
          year='2011', track='main', language='ES'
      ),  # 2011 Main track Spanish (2011.main.ES)
      Qa4mreConfig(
          year='2011', track='main', language='IT'
      ),  # 2011 Main track Italian (2011.main.IT)
      Qa4mreConfig(
          year='2011', track='main', language='RO'
      ),  # 2011 Main track Romanian (2011.main.RO)
      Qa4mreConfig(
          year='2012', track='main', language='AR'
      ),  # 2012 Main track Arabic (2012.main.AR)
      Qa4mreConfig(
          year='2012', track='main', language='BG'
      ),  # 2012 Main track Bulgarian (2012.main.BG)
      Qa4mreConfig(
          year='2012', track='main', language='DE'
      ),  # 2012 Main track German (2012.main.DE)
      Qa4mreConfig(
          year='2012', track='main', language='EN'
      ),  # 2012 Main track English (2012.main.EN)
      Qa4mreConfig(
          year='2012', track='main', language='ES'
      ),  # 2012 Main track Spanish (2012.main.ES)
      Qa4mreConfig(
          year='2012', track='main', language='IT'
      ),  # 2012 Main track Italian (2012.main.IT)
      Qa4mreConfig(
          year='2012', track='main', language='RO'
      ),  # 2012 Main track Romanian (2012.main.RO)
      Qa4mreConfig(
          year='2012', track='alzheimers', language='EN'
      ),  # (2012.alzheimers.EN)
      Qa4mreConfig(
          year='2013', track='main', language='AR'
      ),  # 2013 Main track Arabic (2013.main.AR)
      Qa4mreConfig(
          year='2013', track='main', language='BG'
      ),  # 2013 Main track Bulgarian (2013.main.BG)
      Qa4mreConfig(
          year='2013', track='main', language='EN'
      ),  # 2013 Main track English (2013.main.EN)
      Qa4mreConfig(
          year='2013', track='main', language='ES'
      ),  # 2013 Main track Spanish (2013.main.ES)
      Qa4mreConfig(
          year='2013', track='main', language='RO'
      ),  # 2013 Main track Romanian (2013.main.RO)
      Qa4mreConfig(
          year='2013', track='alzheimers', language='EN'
      ),  # (2013.alzheimers.EN)
      Qa4mreConfig(
          year='2013', track='entrance_exam', language='EN'
      ),  # (2013.entrance_exam.EN)
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'topic_id': tfds.features.Text(),
            'topic_name': tfds.features.Text(),
            'test_id': tfds.features.Text(),
            'document_id': tfds.features.Text(),
            'document_str': tfds.features.Text(),
            'question_id': tfds.features.Text(),
            'question_str': tfds.features.Text(),
            'answer_options': tfds.features.Sequence({
                'answer_id': tfds.features.Text(),
                'answer_str': tfds.features.Text(),
            }),
            'correct_answer_id': tfds.features.Text(),
            'correct_answer_str': tfds.features.Text(),
        }),
        # No default supervised keys because both passage and question are used
        # to determine the correct answer.
        supervised_keys=None,
        homepage='http://nlp.uned.es/clef-qa/repository/pastCampaigns.php',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    cfg = self.builder_config
    download_urls = dict()

    if cfg.track == 'main':
      download_urls['{}.main.{}'.format(cfg.year, cfg.lang)] = os.path.join(
          _BASE_URL, PATHS[cfg.year]['_PATH_TMPL_MAIN_GS'].format(cfg.lang)
      )  # pytype: disable=attribute-error

    if cfg.year in ['2012', '2013'] and cfg.track == 'alzheimers':
      download_urls['{}.alzheimers.EN'.format(cfg.year)] = os.path.join(
          _BASE_URL, PATHS[cfg.year]['_PATH_ALZHEIMER']
      )

    if cfg.year == '2013' and cfg.track == 'entrance_exam':
      download_urls['2013.entrance_exam.EN'] = os.path.join(
          _BASE_URL, PATHS[cfg.year]['_PATH_ENTRANCE_EXAM']
      )

    downloaded_files = dl_manager.download_and_extract(download_urls)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filepath': downloaded_files[
                    '{}.{}.{}'.format(cfg.year, cfg.track, cfg.lang)
                ]
            },
        )
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""
    with tf.io.gfile.GFile(filepath, 'rb') as f:
      tree = ET.parse(f)
      root = tree.getroot()  # test-set
      for topic in root:
        topic_id = topic.attrib['t_id']
        topic_name = topic.attrib['t_name']
        for test in topic:
          test_id = test.attrib['r_id']
          for document in test.iter('doc'):
            document_id = document.attrib['d_id']
            document_str = document.text
          for question in test.iter('q'):
            yield _get_question(
                topic_id,
                topic_name,
                test_id,
                document_id,
                document_str,
                question,
            )
