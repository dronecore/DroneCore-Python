# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core.proto',
  package='mavsdk.rpc.core',
  syntax='proto3',
  serialized_options=_b('\n\026io.mavlink.mavsdk.coreB\tCoreProto'),
  serialized_pb=_b('\n\ncore.proto\x12\x0fmavsdk.rpc.core\"!\n\x1fSubscribeConnectionStateRequest\"U\n\x17\x43onnectionStateResponse\x12:\n\x10\x63onnection_state\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.core.ConnectionState\"\x1b\n\x19ListRunningPluginsRequest\"N\n\x1aListRunningPluginsResponse\x12\x30\n\x0bplugin_info\x18\x01 \x03(\x0b\x32\x1b.mavsdk.rpc.core.PluginInfo\"5\n\x0f\x43onnectionState\x12\x0c\n\x04uuid\x18\x01 \x01(\x04\x12\x14\n\x0cis_connected\x18\x02 \x01(\x08\"9\n\nPluginInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x32\xfa\x01\n\x0b\x43oreService\x12z\n\x18SubscribeConnectionState\x12\x30.mavsdk.rpc.core.SubscribeConnectionStateRequest\x1a(.mavsdk.rpc.core.ConnectionStateResponse\"\x00\x30\x01\x12o\n\x12ListRunningPlugins\x12*.mavsdk.rpc.core.ListRunningPluginsRequest\x1a+.mavsdk.rpc.core.ListRunningPluginsResponse\"\x00\x42#\n\x16io.mavlink.mavsdk.coreB\tCoreProtob\x06proto3')
)




_SUBSCRIBECONNECTIONSTATEREQUEST = _descriptor.Descriptor(
  name='SubscribeConnectionStateRequest',
  full_name='mavsdk.rpc.core.SubscribeConnectionStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=64,
)


_CONNECTIONSTATERESPONSE = _descriptor.Descriptor(
  name='ConnectionStateResponse',
  full_name='mavsdk.rpc.core.ConnectionStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_state', full_name='mavsdk.rpc.core.ConnectionStateResponse.connection_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=151,
)


_LISTRUNNINGPLUGINSREQUEST = _descriptor.Descriptor(
  name='ListRunningPluginsRequest',
  full_name='mavsdk.rpc.core.ListRunningPluginsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=180,
)


_LISTRUNNINGPLUGINSRESPONSE = _descriptor.Descriptor(
  name='ListRunningPluginsResponse',
  full_name='mavsdk.rpc.core.ListRunningPluginsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_info', full_name='mavsdk.rpc.core.ListRunningPluginsResponse.plugin_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=260,
)


_CONNECTIONSTATE = _descriptor.Descriptor(
  name='ConnectionState',
  full_name='mavsdk.rpc.core.ConnectionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='mavsdk.rpc.core.ConnectionState.uuid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_connected', full_name='mavsdk.rpc.core.ConnectionState.is_connected', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=315,
)


_PLUGININFO = _descriptor.Descriptor(
  name='PluginInfo',
  full_name='mavsdk.rpc.core.PluginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mavsdk.rpc.core.PluginInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='mavsdk.rpc.core.PluginInfo.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='mavsdk.rpc.core.PluginInfo.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=374,
)

_CONNECTIONSTATERESPONSE.fields_by_name['connection_state'].message_type = _CONNECTIONSTATE
_LISTRUNNINGPLUGINSRESPONSE.fields_by_name['plugin_info'].message_type = _PLUGININFO
DESCRIPTOR.message_types_by_name['SubscribeConnectionStateRequest'] = _SUBSCRIBECONNECTIONSTATEREQUEST
DESCRIPTOR.message_types_by_name['ConnectionStateResponse'] = _CONNECTIONSTATERESPONSE
DESCRIPTOR.message_types_by_name['ListRunningPluginsRequest'] = _LISTRUNNINGPLUGINSREQUEST
DESCRIPTOR.message_types_by_name['ListRunningPluginsResponse'] = _LISTRUNNINGPLUGINSRESPONSE
DESCRIPTOR.message_types_by_name['ConnectionState'] = _CONNECTIONSTATE
DESCRIPTOR.message_types_by_name['PluginInfo'] = _PLUGININFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeConnectionStateRequest = _reflection.GeneratedProtocolMessageType('SubscribeConnectionStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECONNECTIONSTATEREQUEST,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.core.SubscribeConnectionStateRequest)
  })
_sym_db.RegisterMessage(SubscribeConnectionStateRequest)

ConnectionStateResponse = _reflection.GeneratedProtocolMessageType('ConnectionStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONSTATERESPONSE,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.core.ConnectionStateResponse)
  })
_sym_db.RegisterMessage(ConnectionStateResponse)

ListRunningPluginsRequest = _reflection.GeneratedProtocolMessageType('ListRunningPluginsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRUNNINGPLUGINSREQUEST,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.core.ListRunningPluginsRequest)
  })
_sym_db.RegisterMessage(ListRunningPluginsRequest)

ListRunningPluginsResponse = _reflection.GeneratedProtocolMessageType('ListRunningPluginsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRUNNINGPLUGINSRESPONSE,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.core.ListRunningPluginsResponse)
  })
_sym_db.RegisterMessage(ListRunningPluginsResponse)

ConnectionState = _reflection.GeneratedProtocolMessageType('ConnectionState', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONSTATE,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.core.ConnectionState)
  })
_sym_db.RegisterMessage(ConnectionState)

PluginInfo = _reflection.GeneratedProtocolMessageType('PluginInfo', (_message.Message,), {
  'DESCRIPTOR' : _PLUGININFO,
  '__module__' : 'core_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.core.PluginInfo)
  })
_sym_db.RegisterMessage(PluginInfo)


DESCRIPTOR._options = None

_CORESERVICE = _descriptor.ServiceDescriptor(
  name='CoreService',
  full_name='mavsdk.rpc.core.CoreService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=377,
  serialized_end=627,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeConnectionState',
    full_name='mavsdk.rpc.core.CoreService.SubscribeConnectionState',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBECONNECTIONSTATEREQUEST,
    output_type=_CONNECTIONSTATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListRunningPlugins',
    full_name='mavsdk.rpc.core.CoreService.ListRunningPlugins',
    index=1,
    containing_service=None,
    input_type=_LISTRUNNINGPLUGINSREQUEST,
    output_type=_LISTRUNNINGPLUGINSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CORESERVICE)

DESCRIPTOR.services_by_name['CoreService'] = _CORESERVICE

# @@protoc_insertion_point(module_scope)
