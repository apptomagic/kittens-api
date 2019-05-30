# pylint: disable=function-redefined,no-name-in-module
from behave import given, when, then
import grpc
from client.post_pb2 import *

@when(u'I make a new post with no title and which is not a reply')
def step_impl(context):
  try:
    context.call_res = context.stubs.posts.Create(CreatePostRequest(
      text = 'foo'
    ))
  except grpc.RpcError as e:
    context.call_exc = e


@then(u'It fails, telling me I must provide more data')
def step_impl(context):
  assert hasattr(context, 'call_exc')
  assert context.call_exc.code() == grpc.StatusCode.INVALID_ARGUMENT
  assert context.call_exc.details() == "Replies need inReplyTo, OPs need conversationTitle"


@when(u'I make a new post and don\'t provide an author name')
def step_impl(context):
  context.call_res = context.stubs.posts.Create(CreatePostRequest(
    text = 'foo',
    conversationTitle = 'Foo'
  ))


@then(u'My new post is created')
def step_impl(context):
  assert isinstance(context.call_res, Post)


@then(u'The author display name is "{authorDisplayName}"')
def step_impl(context, authorDisplayName):
  assert context.call_res.authorDisplayName == authorDisplayName


@given(u'I\'m authenticated as {userId}')
def step_impl(context, userId):
  for ctx in context.active_contexts:
    try:
      users = ctx['data']['users']
    except KeyError:
      continue
    for user in users:
      if user['id'] == userId:
        context.auth_user = user
        return
  assert False, 'User {} not found in provided contexts'.format(userId)


@when(u'I make a new post')
def step_impl(context):
  context.call_res = context.stubs.posts.Create(CreatePostRequest(
    text = 'foo',
    conversationTitle = 'Foo',
    authorDisplayName = context.auth_user['displayName']
  ))


# @when(u'I fetch all posts by {userId}')
# def step_impl(context, userId):
#   pass


# @then(u'I get {num:d} posts')
# def step_impl(context, num):
#   pass


# @when(u'I fetch the thread from {postId} after {postId2}')
# def step_impl(context, postId, postId2):
#   pass


# @when(u'I fetch the thread from {postId} since {timestamp}')
# def step_impl(context, postId, timestamp):
#   pass


# @when(u'I fetch the thread from {postId}')
# def step_impl(context, postId):
#   pass
