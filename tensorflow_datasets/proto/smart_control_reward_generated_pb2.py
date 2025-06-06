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

# pylint: skip-file

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart_control_reward.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1asmart_control_reward.proto\x12#smart_buildings.smart_control.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe9\t\n\nRewardInfo\x12\x33\n\x0fstart_timestamp\x18\x01'
    b' \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x02'
    b' \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x61gent_id\x18\x03'
    b' \x01(\t\x12\x13\n\x0bscenario_id\x18\x04'
    b' \x01(\t\x12_\n\x11zone_reward_infos\x18\x05'
    b' \x03(\x0b\x32\x44.smart_buildings.smart_control.proto.RewardInfo.ZoneRewardInfosEntry\x12l\n\x18\x61ir_handler_reward_infos\x18\x06'
    b' \x03(\x0b\x32J.smart_buildings.smart_control.proto.RewardInfo.AirHandlerRewardInfosEntry\x12\x63\n\x13\x62oiler_reward_infos\x18\x07'
    b' \x03(\x0b\x32\x46.smart_buildings.smart_control.proto.RewardInfo.BoilerRewardInfosEntry\x1a\xcc\x01\n\x0eZoneRewardInfo\x12$\n\x1cheating_setpoint_temperature\x18\x01'
    b' \x01(\x02\x12$\n\x1c\x63ooling_setpoint_temperature\x18\x02'
    b' \x01(\x02\x12\x1c\n\x14zone_air_temperature\x18\x03'
    b' \x01(\x02\x12\x1e\n\x16\x61ir_flow_rate_setpoint\x18\x04'
    b' \x01(\x02\x12\x15\n\rair_flow_rate\x18\x05'
    b' \x01(\x02\x12\x19\n\x11\x61verage_occupancy\x18\x06'
    b' \x01(\x02\x1an\n\x14\x41irHandlerRewardInfo\x12%\n\x1d\x62lower_electrical_energy_rate\x18\x01'
    b" \x01(\x02\x12/\n'air_conditioning_electrical_energy_rate\x18\x02"
    b" \x01(\x02\x1a`\n\x10\x42oilerRewardInfo\x12'\n\x1fnatural_gas_heating_energy_rate\x18\x01"
    b' \x01(\x02\x12#\n\x1bpump_electrical_energy_rate\x18\x02'
    b' \x01(\x02\x1av\n\x14ZoneRewardInfosEntry\x12\x0b\n\x03key\x18\x01'
    b' \x01(\t\x12M\n\x05value\x18\x02'
    b' \x01(\x0b\x32>.smart_buildings.smart_control.proto.RewardInfo.ZoneRewardInfo:\x02\x38\x01\x1a\x82\x01\n\x1a\x41irHandlerRewardInfosEntry\x12\x0b\n\x03key\x18\x01'
    b' \x01(\t\x12S\n\x05value\x18\x02'
    b' \x01(\x0b\x32\x44.smart_buildings.smart_control.proto.RewardInfo.AirHandlerRewardInfo:\x02\x38\x01\x1az\n\x16\x42oilerRewardInfosEntry\x12\x0b\n\x03key\x18\x01'
    b' \x01(\t\x12O\n\x05value\x18\x02'
    b' \x01(\x0b\x32@.smart_buildings.smart_control.proto.RewardInfo.BoilerRewardInfo:\x02\x38\x01"\xe4\x04\n\x0eRewardResponse\x12\x1a\n\x12\x61gent_reward_value\x18\x01'
    b' \x01(\x02\x12\x1b\n\x13productivity_reward\x18\x02'
    b' \x01(\x02\x12\x1f\n\x17\x65lectricity_energy_cost\x18\x03'
    b' \x01(\x02\x12\x1f\n\x17natural_gas_energy_cost\x18\x04'
    b' \x01(\x02\x12\x16\n\x0e\x63\x61rbon_emitted\x18\x05'
    b' \x01(\x02\x12\x13\n\x0b\x63\x61rbon_cost\x18\x06'
    b' \x01(\x02\x12\x1b\n\x13productivity_weight\x18\x07'
    b' \x01(\x02\x12\x1a\n\x12\x65nergy_cost_weight\x18\x08'
    b' \x01(\x02\x12\x1e\n\x16\x63\x61rbon_emission_weight\x18\t'
    b' \x01(\x02\x12\x1b\n\x13person_productivity\x18\n'
    b' \x01(\x02\x12\x17\n\x0ftotal_occupancy\x18\x0b'
    b' \x01(\x02\x12\x14\n\x0creward_scale\x18\x0c'
    b' \x01(\x02\x12\x14\n\x0creward_shift\x18\r'
    b' \x01(\x02\x12\x1b\n\x13productivity_regret\x18\x0e'
    b' \x01(\x02\x12&\n\x1enormalized_productivity_regret\x18\x0f'
    b' \x01(\x02\x12\x1e\n\x16normalized_energy_cost\x18\x10'
    b' \x01(\x02\x12"\n\x1anormalized_carbon_emission\x18\x11'
    b' \x01(\x02\x12\x33\n\x0fstart_timestamp\x18\x12'
    b' \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x13'
    b' \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'smart_control_reward_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REWARDINFO_ZONEREWARDINFOSENTRY._options = None
  _REWARDINFO_ZONEREWARDINFOSENTRY._serialized_options = b'8\001'
  _REWARDINFO_AIRHANDLERREWARDINFOSENTRY._options = None
  _REWARDINFO_AIRHANDLERREWARDINFOSENTRY._serialized_options = b'8\001'
  _REWARDINFO_BOILERREWARDINFOSENTRY._options = None
  _REWARDINFO_BOILERREWARDINFOSENTRY._serialized_options = b'8\001'
  _REWARDINFO._serialized_start = 101
  _REWARDINFO._serialized_end = 1358
  _REWARDINFO_ZONEREWARDINFO._serialized_start = 567
  _REWARDINFO_ZONEREWARDINFO._serialized_end = 771
  _REWARDINFO_AIRHANDLERREWARDINFO._serialized_start = 773
  _REWARDINFO_AIRHANDLERREWARDINFO._serialized_end = 883
  _REWARDINFO_BOILERREWARDINFO._serialized_start = 885
  _REWARDINFO_BOILERREWARDINFO._serialized_end = 981
  _REWARDINFO_ZONEREWARDINFOSENTRY._serialized_start = 983
  _REWARDINFO_ZONEREWARDINFOSENTRY._serialized_end = 1101
  _REWARDINFO_AIRHANDLERREWARDINFOSENTRY._serialized_start = 1104
  _REWARDINFO_AIRHANDLERREWARDINFOSENTRY._serialized_end = 1234
  _REWARDINFO_BOILERREWARDINFOSENTRY._serialized_start = 1236
  _REWARDINFO_BOILERREWARDINFOSENTRY._serialized_end = 1358
  _REWARDRESPONSE._serialized_start = 1361
  _REWARDRESPONSE._serialized_end = 1973
# @@protoc_insertion_point(module_scope)
