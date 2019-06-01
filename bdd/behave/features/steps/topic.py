# pylint: disable=function-redefined,no-name-in-module
from behave import given, when, then
import grpc
from google.protobuf.empty_pb2 import Empty
from client.topic_pb2 import *


@when(u'I fetch all topics')
def step_impl(context):
  context.stubs.try_call(
    context.stubs.topics.AllTopics,
    Empty(),
  )


@when(u'I fetch topics related to "{name}"')
def step_impl(context, name):
  context.stubs.try_call(
    context.stubs.topics.Related,
    TopicRequest(name=name),
  )


@then(u'I get {num:d} topics')
def step_impl(context, num):
  topics = list(context.stubs.call_res)
  assert len(topics) == num, 'got {} topics'.format(len(topics))
