# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\"\\\n\nRequestMsg\x12\x13\n\x06\x66ield1\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06\x66ield2\x18\x02 \x01(\x05\x12\x0e\n\x06\x66ield3\x18\x03 \x01(\x01\x12\x0e\n\x06\x66ield4\x18\x04 \x03(\tB\t\n\x07_field1\"2\n\x08ReplyMsg\x12\x17\n\nhelloworld\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_helloworld25\n\x0bGRPCExample\x12&\n\nHelloWorld\x12\x0b.RequestMsg\x1a\t.ReplyMsg\"\x00\x62\x06proto3')



_REQUESTMSG = DESCRIPTOR.message_types_by_name['RequestMsg']
_REPLYMSG = DESCRIPTOR.message_types_by_name['ReplyMsg']
RequestMsg = _reflection.GeneratedProtocolMessageType('RequestMsg', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMSG,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:RequestMsg)
  })
_sym_db.RegisterMessage(RequestMsg)

ReplyMsg = _reflection.GeneratedProtocolMessageType('ReplyMsg', (_message.Message,), {
  'DESCRIPTOR' : _REPLYMSG,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:ReplyMsg)
  })
_sym_db.RegisterMessage(ReplyMsg)

_GRPCEXAMPLE = DESCRIPTOR.services_by_name['GRPCExample']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTMSG._serialized_start=15
  _REQUESTMSG._serialized_end=107
  _REPLYMSG._serialized_start=109
  _REPLYMSG._serialized_end=159
  _GRPCEXAMPLE._serialized_start=161
  _GRPCEXAMPLE._serialized_end=214
# @@protoc_insertion_point(module_scope)
