# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: conversation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import post_pb2 as post__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='conversation.proto',
  package='kittens.conversation',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x63onversation.proto\x12\x14kittens.conversation\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\npost.proto\"!\n\x05Topic\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"G\n\x0c\x43onversation\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04opId\x18\x03 \x01(\t\x12\x0e\n\x06topics\x18\x04 \x03(\t\"H\n\x19\x43reateConversationRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06topics\x18\x02 \x03(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\"m\n\x11\x43onversationAndOP\x12\x38\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\".kittens.conversation.Conversation\x12\x1e\n\x02op\x18\x02 \x01(\x0b\x32\x12.kittens.post.Post\"u\n\x1b\x43onversationsByTopicRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\r\n\x05watch\x18\x02 \x01(\x08\x12\r\n\x05\x61\x66ter\x18\x03 \x01(\t\x12)\n\x05since\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"^\n\x13SetupContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\rconversations\x18\x02 \x03(\x0b\x32\".kittens.conversation.Conversation2\xaf\x02\n\rConversations\x12\x62\n\x06\x43reate\x12/.kittens.conversation.CreateConversationRequest\x1a\'.kittens.conversation.ConversationAndOP\x12g\n\x07\x42yTopic\x12\x31.kittens.conversation.ConversationsByTopicRequest\x1a\'.kittens.conversation.ConversationAndOP0\x01\x12Q\n\x0cSetupContext\x12).kittens.conversation.SetupContextRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,post__pb2.DESCRIPTOR,])




_TOPIC = _descriptor.Descriptor(
  name='Topic',
  full_name='kittens.conversation.Topic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kittens.conversation.Topic.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='kittens.conversation.Topic.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=118,
  serialized_end=151,
)


_CONVERSATION = _descriptor.Descriptor(
  name='Conversation',
  full_name='kittens.conversation.Conversation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kittens.conversation.Conversation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='kittens.conversation.Conversation.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opId', full_name='kittens.conversation.Conversation.opId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topics', full_name='kittens.conversation.Conversation.topics', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=153,
  serialized_end=224,
)


_CREATECONVERSATIONREQUEST = _descriptor.Descriptor(
  name='CreateConversationRequest',
  full_name='kittens.conversation.CreateConversationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='kittens.conversation.CreateConversationRequest.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topics', full_name='kittens.conversation.CreateConversationRequest.topics', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='kittens.conversation.CreateConversationRequest.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=226,
  serialized_end=298,
)


_CONVERSATIONANDOP = _descriptor.Descriptor(
  name='ConversationAndOP',
  full_name='kittens.conversation.ConversationAndOP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversation', full_name='kittens.conversation.ConversationAndOP.conversation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='kittens.conversation.ConversationAndOP.op', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=300,
  serialized_end=409,
)


_CONVERSATIONSBYTOPICREQUEST = _descriptor.Descriptor(
  name='ConversationsByTopicRequest',
  full_name='kittens.conversation.ConversationsByTopicRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='kittens.conversation.ConversationsByTopicRequest.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='watch', full_name='kittens.conversation.ConversationsByTopicRequest.watch', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='kittens.conversation.ConversationsByTopicRequest.after', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since', full_name='kittens.conversation.ConversationsByTopicRequest.since', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=411,
  serialized_end=528,
)


_SETUPCONTEXTREQUEST = _descriptor.Descriptor(
  name='SetupContextRequest',
  full_name='kittens.conversation.SetupContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kittens.conversation.SetupContextRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversations', full_name='kittens.conversation.SetupContextRequest.conversations', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=530,
  serialized_end=624,
)

_CONVERSATIONANDOP.fields_by_name['conversation'].message_type = _CONVERSATION
_CONVERSATIONANDOP.fields_by_name['op'].message_type = post__pb2._POST
_CONVERSATIONSBYTOPICREQUEST.fields_by_name['since'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SETUPCONTEXTREQUEST.fields_by_name['conversations'].message_type = _CONVERSATION
DESCRIPTOR.message_types_by_name['Topic'] = _TOPIC
DESCRIPTOR.message_types_by_name['Conversation'] = _CONVERSATION
DESCRIPTOR.message_types_by_name['CreateConversationRequest'] = _CREATECONVERSATIONREQUEST
DESCRIPTOR.message_types_by_name['ConversationAndOP'] = _CONVERSATIONANDOP
DESCRIPTOR.message_types_by_name['ConversationsByTopicRequest'] = _CONVERSATIONSBYTOPICREQUEST
DESCRIPTOR.message_types_by_name['SetupContextRequest'] = _SETUPCONTEXTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Topic = _reflection.GeneratedProtocolMessageType('Topic', (_message.Message,), dict(
  DESCRIPTOR = _TOPIC,
  __module__ = 'conversation_pb2'
  # @@protoc_insertion_point(class_scope:kittens.conversation.Topic)
  ))
_sym_db.RegisterMessage(Topic)

Conversation = _reflection.GeneratedProtocolMessageType('Conversation', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSATION,
  __module__ = 'conversation_pb2'
  # @@protoc_insertion_point(class_scope:kittens.conversation.Conversation)
  ))
_sym_db.RegisterMessage(Conversation)

CreateConversationRequest = _reflection.GeneratedProtocolMessageType('CreateConversationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATECONVERSATIONREQUEST,
  __module__ = 'conversation_pb2'
  # @@protoc_insertion_point(class_scope:kittens.conversation.CreateConversationRequest)
  ))
_sym_db.RegisterMessage(CreateConversationRequest)

ConversationAndOP = _reflection.GeneratedProtocolMessageType('ConversationAndOP', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSATIONANDOP,
  __module__ = 'conversation_pb2'
  # @@protoc_insertion_point(class_scope:kittens.conversation.ConversationAndOP)
  ))
_sym_db.RegisterMessage(ConversationAndOP)

ConversationsByTopicRequest = _reflection.GeneratedProtocolMessageType('ConversationsByTopicRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSATIONSBYTOPICREQUEST,
  __module__ = 'conversation_pb2'
  # @@protoc_insertion_point(class_scope:kittens.conversation.ConversationsByTopicRequest)
  ))
_sym_db.RegisterMessage(ConversationsByTopicRequest)

SetupContextRequest = _reflection.GeneratedProtocolMessageType('SetupContextRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETUPCONTEXTREQUEST,
  __module__ = 'conversation_pb2'
  # @@protoc_insertion_point(class_scope:kittens.conversation.SetupContextRequest)
  ))
_sym_db.RegisterMessage(SetupContextRequest)



_CONVERSATIONS = _descriptor.ServiceDescriptor(
  name='Conversations',
  full_name='kittens.conversation.Conversations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=627,
  serialized_end=930,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='kittens.conversation.Conversations.Create',
    index=0,
    containing_service=None,
    input_type=_CREATECONVERSATIONREQUEST,
    output_type=_CONVERSATIONANDOP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ByTopic',
    full_name='kittens.conversation.Conversations.ByTopic',
    index=1,
    containing_service=None,
    input_type=_CONVERSATIONSBYTOPICREQUEST,
    output_type=_CONVERSATIONANDOP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetupContext',
    full_name='kittens.conversation.Conversations.SetupContext',
    index=2,
    containing_service=None,
    input_type=_SETUPCONTEXTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONVERSATIONS)

DESCRIPTOR.services_by_name['Conversations'] = _CONVERSATIONS

# @@protoc_insertion_point(module_scope)
