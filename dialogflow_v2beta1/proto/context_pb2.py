# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2beta1/proto/context.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow_v2beta1/proto/context.proto',
  package='google.cloud.dialogflow.v2beta1',
  syntax='proto3',
  serialized_pb=_b('\n3google/cloud/dialogflow_v2beta1/proto/context.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\"\\\n\x07\x43ontext\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0elifespan_count\x18\x02 \x01(\x05\x12+\n\nparameters\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"L\n\x13ListContextsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"k\n\x14ListContextsResponse\x12:\n\x08\x63ontexts\x18\x01 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.Context\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"!\n\x11GetContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"a\n\x14\x43reateContextRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x39\n\x07\x63ontext\x18\x02 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.Context\"\x82\x01\n\x14UpdateContextRequest\x12\x39\n\x07\x63ontext\x18\x01 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.Context\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"$\n\x14\x44\x65leteContextRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"*\n\x18\x44\x65leteAllContextsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t2\xcb\x0c\n\x08\x43ontexts\x12\x8e\x02\n\x0cListContexts\x12\x34.google.cloud.dialogflow.v2beta1.ListContextsRequest\x1a\x35.google.cloud.dialogflow.v2beta1.ListContextsResponse\"\x90\x01\x82\xd3\xe4\x93\x02\x89\x01\x12\x36/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO\x12M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts\x12\xfd\x01\n\nGetContext\x12\x32.google.cloud.dialogflow.v2beta1.GetContextRequest\x1a(.google.cloud.dialogflow.v2beta1.Context\"\x90\x01\x82\xd3\xe4\x93\x02\x89\x01\x12\x36/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO\x12M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}\x12\x95\x02\n\rCreateContext\x12\x35.google.cloud.dialogflow.v2beta1.CreateContextRequest\x1a(.google.cloud.dialogflow.v2beta1.Context\"\xa2\x01\x82\xd3\xe4\x93\x02\x9b\x01\"6/v2beta1/{parent=projects/*/agent/sessions/*}/contexts:\x07\x63ontextZX\"M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts:\x07\x63ontext\x12\xa5\x02\n\rUpdateContext\x12\x35.google.cloud.dialogflow.v2beta1.UpdateContextRequest\x1a(.google.cloud.dialogflow.v2beta1.Context\"\xb2\x01\x82\xd3\xe4\x93\x02\xab\x01\x32>/v2beta1/{context.name=projects/*/agent/sessions/*/contexts/*}:\x07\x63ontextZ`2U/v2beta1/{context.name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}:\x07\x63ontext\x12\xf1\x01\n\rDeleteContext\x12\x35.google.cloud.dialogflow.v2beta1.DeleteContextRequest\x1a\x16.google.protobuf.Empty\"\x90\x01\x82\xd3\xe4\x93\x02\x89\x01*6/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO*M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}\x12\xf9\x01\n\x11\x44\x65leteAllContexts\x12\x39.google.cloud.dialogflow.v2beta1.DeleteAllContextsRequest\x1a\x16.google.protobuf.Empty\"\x90\x01\x82\xd3\xe4\x93\x02\x89\x01*6/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO*M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contextsB\xaa\x01\n#com.google.cloud.dialogflow.v2beta1B\x0c\x43ontextProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='google.cloud.dialogflow.v2beta1.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.Context.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifespan_count', full_name='google.cloud.dialogflow.v2beta1.Context.lifespan_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='google.cloud.dialogflow.v2beta1.Context.parameters', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=303,
)


_LISTCONTEXTSREQUEST = _descriptor.Descriptor(
  name='ListContextsRequest',
  full_name='google.cloud.dialogflow.v2beta1.ListContextsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.ListContextsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dialogflow.v2beta1.ListContextsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dialogflow.v2beta1.ListContextsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=381,
)


_LISTCONTEXTSRESPONSE = _descriptor.Descriptor(
  name='ListContextsResponse',
  full_name='google.cloud.dialogflow.v2beta1.ListContextsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contexts', full_name='google.cloud.dialogflow.v2beta1.ListContextsResponse.contexts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dialogflow.v2beta1.ListContextsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=490,
)


_GETCONTEXTREQUEST = _descriptor.Descriptor(
  name='GetContextRequest',
  full_name='google.cloud.dialogflow.v2beta1.GetContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.GetContextRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=525,
)


_CREATECONTEXTREQUEST = _descriptor.Descriptor(
  name='CreateContextRequest',
  full_name='google.cloud.dialogflow.v2beta1.CreateContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.CreateContextRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='google.cloud.dialogflow.v2beta1.CreateContextRequest.context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=624,
)


_UPDATECONTEXTREQUEST = _descriptor.Descriptor(
  name='UpdateContextRequest',
  full_name='google.cloud.dialogflow.v2beta1.UpdateContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='google.cloud.dialogflow.v2beta1.UpdateContextRequest.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.dialogflow.v2beta1.UpdateContextRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=757,
)


_DELETECONTEXTREQUEST = _descriptor.Descriptor(
  name='DeleteContextRequest',
  full_name='google.cloud.dialogflow.v2beta1.DeleteContextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2beta1.DeleteContextRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=795,
)


_DELETEALLCONTEXTSREQUEST = _descriptor.Descriptor(
  name='DeleteAllContextsRequest',
  full_name='google.cloud.dialogflow.v2beta1.DeleteAllContextsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2beta1.DeleteAllContextsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=797,
  serialized_end=839,
)

_CONTEXT.fields_by_name['parameters'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LISTCONTEXTSRESPONSE.fields_by_name['contexts'].message_type = _CONTEXT
_CREATECONTEXTREQUEST.fields_by_name['context'].message_type = _CONTEXT
_UPDATECONTEXTREQUEST.fields_by_name['context'].message_type = _CONTEXT
_UPDATECONTEXTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['ListContextsRequest'] = _LISTCONTEXTSREQUEST
DESCRIPTOR.message_types_by_name['ListContextsResponse'] = _LISTCONTEXTSRESPONSE
DESCRIPTOR.message_types_by_name['GetContextRequest'] = _GETCONTEXTREQUEST
DESCRIPTOR.message_types_by_name['CreateContextRequest'] = _CREATECONTEXTREQUEST
DESCRIPTOR.message_types_by_name['UpdateContextRequest'] = _UPDATECONTEXTREQUEST
DESCRIPTOR.message_types_by_name['DeleteContextRequest'] = _DELETECONTEXTREQUEST
DESCRIPTOR.message_types_by_name['DeleteAllContextsRequest'] = _DELETEALLCONTEXTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """Represents a context.
  
  
  Attributes:
      name:
          Required. The unique identifier of the context. Format:
          ``projects/<Project ID>/agent/sessions/<Session
          ID>/contexts/<Context ID>``, or ``projects/<Project
          ID>/agent/environments/<Environment ID>/users/<User
          ID>/sessions/<Session ID>/contexts/<Context ID>``. Note:
          Environments and users are under construction and will be
          available soon. The Context ID is always converted to
          lowercase. If is not specified, we assume default 'draft'
          environment. If is not specified, we assume default '-' user.
      lifespan_count:
          Optional. The number of conversational query requests after
          which the context expires. If set to ``0`` (the default) the
          context expires immediately. Contexts expire automatically
          after 10 minutes even if there are no matching queries.
      parameters:
          Optional. The collection of parameters associated with this
          context. Refer to `this doc
          <https://dialogflow.com/docs/actions-and-parameters>`__ for
          syntax.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.Context)
  ))
_sym_db.RegisterMessage(Context)

ListContextsRequest = _reflection.GeneratedProtocolMessageType('ListContextsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCONTEXTSREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """The request message for
  [Contexts.ListContexts][google.cloud.dialogflow.v2beta1.Contexts.ListContexts].
  
  
  Attributes:
      parent:
          Required. The session to list all contexts from. Format:
          ``projects/<Project ID>/agent/sessions/<Session ID>`` or
          ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>``. Note:
          Environments and users are under construction and will be
          available soon. If is not specified, we assume default 'draft'
          environment. If is not specified, we assume default '-' user.
      page_size:
          Optional. The maximum number of items to return in a single
          page. By default 100 and at most 1000.
      page_token:
          Optional. The next\_page\_token value returned from a previous
          list request.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListContextsRequest)
  ))
_sym_db.RegisterMessage(ListContextsRequest)

ListContextsResponse = _reflection.GeneratedProtocolMessageType('ListContextsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCONTEXTSRESPONSE,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """The response message for
  [Contexts.ListContexts][google.cloud.dialogflow.v2beta1.Contexts.ListContexts].
  
  
  Attributes:
      contexts:
          The list of contexts. There will be a maximum number of items
          returned based on the page\_size field in the request.
      next_page_token:
          Token to retrieve the next page of results, or empty if there
          are no more results in the list.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListContextsResponse)
  ))
_sym_db.RegisterMessage(ListContextsResponse)

GetContextRequest = _reflection.GeneratedProtocolMessageType('GetContextRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONTEXTREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """The request message for
  [Contexts.GetContext][google.cloud.dialogflow.v2beta1.Contexts.GetContext].
  
  
  Attributes:
      name:
          Required. The name of the context. Format: ``projects/<Project
          ID>/agent/sessions/<Session ID>/contexts/<Context ID>`` or
          ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>/contexts/<Context
          ID>``. Note: Environments and users are under construction and
          will be available soon. If is not specified, we assume default
          'draft' environment. If is not specified, we assume default
          '-' user.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.GetContextRequest)
  ))
_sym_db.RegisterMessage(GetContextRequest)

CreateContextRequest = _reflection.GeneratedProtocolMessageType('CreateContextRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATECONTEXTREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """The request message for
  [Contexts.CreateContext][google.cloud.dialogflow.v2beta1.Contexts.CreateContext].
  
  
  Attributes:
      parent:
          Required. The session to create a context for. Format:
          ``projects/<Project ID>/agent/sessions/<Session ID>`` or
          ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>``. Note:
          Environments and users are under construction and will be
          available soon. If is not specified, we assume default 'draft'
          environment. If is not specified, we assume default '-' user.
      context:
          Required. The context to create.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CreateContextRequest)
  ))
_sym_db.RegisterMessage(CreateContextRequest)

UpdateContextRequest = _reflection.GeneratedProtocolMessageType('UpdateContextRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECONTEXTREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """The request message for
  [Contexts.UpdateContext][google.cloud.dialogflow.v2beta1.Contexts.UpdateContext].
  
  
  Attributes:
      context:
          Required. The context to update.
      update_mask:
          Optional. The mask to control which fields get updated.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.UpdateContextRequest)
  ))
_sym_db.RegisterMessage(UpdateContextRequest)

DeleteContextRequest = _reflection.GeneratedProtocolMessageType('DeleteContextRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETECONTEXTREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """The request message for
  [Contexts.DeleteContext][google.cloud.dialogflow.v2beta1.Contexts.DeleteContext].
  
  
  Attributes:
      name:
          Required. The name of the context to delete. Format:
          ``projects/<Project ID>/agent/sessions/<Session
          ID>/contexts/<Context ID>`` or ``projects/<Project
          ID>/agent/environments/<Environment ID>/users/<User
          ID>/sessions/<Session ID>/contexts/<Context ID>``. Note:
          Environments and users are under construction and will be
          available soon. If is not specified, we assume default 'draft'
          environment. If is not specified, we assume default '-' user.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DeleteContextRequest)
  ))
_sym_db.RegisterMessage(DeleteContextRequest)

DeleteAllContextsRequest = _reflection.GeneratedProtocolMessageType('DeleteAllContextsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEALLCONTEXTSREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.context_pb2'
  ,
  __doc__ = """The request message for
  [Contexts.DeleteAllContexts][google.cloud.dialogflow.v2beta1.Contexts.DeleteAllContexts].
  
  
  Attributes:
      parent:
          Required. The name of the session to delete all contexts from.
          Format: ``projects/<Project ID>/agent/sessions/<Session ID>``
          or ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>``. Note:
          Environments and users are under construction and will be
          available soon. If is not specified we assume default 'draft'
          environment. If is not specified, we assume default '-' user.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.DeleteAllContextsRequest)
  ))
_sym_db.RegisterMessage(DeleteAllContextsRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.google.cloud.dialogflow.v2beta1B\014ContextProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1'))

_CONTEXTS = _descriptor.ServiceDescriptor(
  name='Contexts',
  full_name='google.cloud.dialogflow.v2beta1.Contexts',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=842,
  serialized_end=2453,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListContexts',
    full_name='google.cloud.dialogflow.v2beta1.Contexts.ListContexts',
    index=0,
    containing_service=None,
    input_type=_LISTCONTEXTSREQUEST,
    output_type=_LISTCONTEXTSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\211\001\0226/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO\022M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts')),
  ),
  _descriptor.MethodDescriptor(
    name='GetContext',
    full_name='google.cloud.dialogflow.v2beta1.Contexts.GetContext',
    index=1,
    containing_service=None,
    input_type=_GETCONTEXTREQUEST,
    output_type=_CONTEXT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\211\001\0226/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO\022M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='CreateContext',
    full_name='google.cloud.dialogflow.v2beta1.Contexts.CreateContext',
    index=2,
    containing_service=None,
    input_type=_CREATECONTEXTREQUEST,
    output_type=_CONTEXT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\233\001\"6/v2beta1/{parent=projects/*/agent/sessions/*}/contexts:\007contextZX\"M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts:\007context')),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateContext',
    full_name='google.cloud.dialogflow.v2beta1.Contexts.UpdateContext',
    index=3,
    containing_service=None,
    input_type=_UPDATECONTEXTREQUEST,
    output_type=_CONTEXT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\253\0012>/v2beta1/{context.name=projects/*/agent/sessions/*/contexts/*}:\007contextZ`2U/v2beta1/{context.name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}:\007context')),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteContext',
    full_name='google.cloud.dialogflow.v2beta1.Contexts.DeleteContext',
    index=4,
    containing_service=None,
    input_type=_DELETECONTEXTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\211\001*6/v2beta1/{name=projects/*/agent/sessions/*/contexts/*}ZO*M/v2beta1/{name=projects/*/agent/environments/*/users/*/sessions/*/contexts/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAllContexts',
    full_name='google.cloud.dialogflow.v2beta1.Contexts.DeleteAllContexts',
    index=5,
    containing_service=None,
    input_type=_DELETEALLCONTEXTSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\211\001*6/v2beta1/{parent=projects/*/agent/sessions/*}/contextsZO*M/v2beta1/{parent=projects/*/agent/environments/*/users/*/sessions/*}/contexts')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTEXTS)

DESCRIPTOR.services_by_name['Contexts'] = _CONTEXTS

# @@protoc_insertion_point(module_scope)