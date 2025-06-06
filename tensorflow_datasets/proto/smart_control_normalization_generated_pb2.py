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
# source: smart_control_normalization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n!smart_control_normalization.proto\x12#smart_buildings.smart_control.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x90\x02\n\x16\x43ontinuousVariableInfo\x12\n\n\x02id\x18\x01'
    b' \x01(\t\x12\x30\n\x0csample_start\x18\x02'
    b' \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nsample_end\x18\x03'
    b' \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bsample_size\x18\x04'
    b' \x01(\x05\x12\x17\n\x0fsample_variance\x18\x05'
    b' \x01(\x02\x12\x13\n\x0bsample_mean\x18\x06'
    b' \x01(\x02\x12\x15\n\rsample_median\x18\x07'
    b' \x01(\x02\x12\x16\n\x0esample_maximum\x18\x08'
    b' \x01(\x02\x12\x16\n\x0esample_minimum\x18\t \x01(\x02\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'smart_control_normalization_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTINUOUSVARIABLEINFO._serialized_start = 108
  _CONTINUOUSVARIABLEINFO._serialized_end = 380
# @@protoc_insertion_point(module_scope)
