# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\x12\x05hello\">\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x05\x12\x13\n\x0bhas_boolean\x18\x03 \x01(\x08\"G\n\x07Request\x12\x0e\n\x06prompt\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\"\x19\n\x08Response\x12\r\n\x05image\x18\x01 \x01(\x0c\">\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x13\n\x0bhas_boolean\x18\x03 \x01(\x08\x32o\n\x07Greeter\x12\x34\n\x08SayHello\x12\x13.hello.HelloRequest\x1a\x11.hello.HelloReply\"\x00\x12.\n\tDiffusion\x12\x0e.hello.Request\x1a\x0f.hello.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=22
  _globals['_HELLOREQUEST']._serialized_end=84
  _globals['_REQUEST']._serialized_start=86
  _globals['_REQUEST']._serialized_end=157
  _globals['_RESPONSE']._serialized_start=159
  _globals['_RESPONSE']._serialized_end=184
  _globals['_HELLOREPLY']._serialized_start=186
  _globals['_HELLOREPLY']._serialized_end=248
  _globals['_GREETER']._serialized_start=250
  _globals['_GREETER']._serialized_end=361
# @@protoc_insertion_point(module_scope)
