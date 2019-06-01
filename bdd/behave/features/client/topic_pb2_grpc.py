# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import topic_pb2 as topic__pb2


class TopicsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AllTopics = channel.unary_unary(
        '/kittens.topic.Topics/AllTopics',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=topic__pb2.TopicList.FromString,
        )
    self.Related = channel.unary_unary(
        '/kittens.topic.Topics/Related',
        request_serializer=topic__pb2.TopicRequest.SerializeToString,
        response_deserializer=topic__pb2.TopicList.FromString,
        )


class TopicsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AllTopics(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Related(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TopicsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AllTopics': grpc.unary_unary_rpc_method_handler(
          servicer.AllTopics,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=topic__pb2.TopicList.SerializeToString,
      ),
      'Related': grpc.unary_unary_rpc_method_handler(
          servicer.Related,
          request_deserializer=topic__pb2.TopicRequest.FromString,
          response_serializer=topic__pb2.TopicList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kittens.topic.Topics', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))