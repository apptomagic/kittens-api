# pylint: disable=function-redefined,no-name-in-module
import grpc
from behave import given, when, then
from client.post_pb2 import *
from client.conversation_pb2 import *


@when(u'I start a conversation without title')
def step_impl(context):
  req = CreateConversationRequest(
    topics = ['foo'],
    text = 'Foo Bar',
  )
  context.try_type = 'Conversations'
  context.stubs.try_call(
    context.stubs.conversations.Create,
    req,
    catch_error = True,
  )


@when(u'I start a conversation without text')
def step_impl(context):
  req = CreateConversationRequest(
    title = 'Foo',
    topics = ['foo'],
  )
  context.try_type = 'Conversations'
  context.stubs.try_call(
    context.stubs.conversations.Create,
    req,
    catch_error = True,
  )


@when(u'I start a conversation without topics')
def step_impl(context):
  req = CreateConversationRequest(
    title = 'Foo',
    text = 'Foo Bar',
  )
  context.try_type = 'Conversations'
  context.stubs.try_call(
    context.stubs.conversations.Create,
    req,
    catch_error = True,
  )


@when(u'I start a conversation')
def step_impl(context):
  req = CreateConversationRequest(
    title = 'Foo',
    topics = ['foo'],
    text = 'Foo Bar',
  )
  if getattr(context, 'auth_user', None):
    req.authorDisplayName = context.auth_user['displayName']
  context.try_type = 'Conversations'
  context.stubs.try_call(
    context.stubs.conversations.Create,
    req,
  )
