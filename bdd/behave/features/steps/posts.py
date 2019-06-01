# pylint: disable=function-redefined,no-name-in-module
from behave import given, when, then
import grpc
from client.post_pb2 import *

@when(u'I make a post without a conversation')
def step_impl(context):
  context.try_type = 'Posts'
  context.stubs.try_call(
    context.stubs.posts.Create,
    CreatePostRequest(text = 'foo'),
    catch_error = True,
  )


@when(u'I make a new post and don\'t provide an author name')
def step_impl(context):
  context.stubs.try_call(
    context.stubs.posts.Create,
    CreatePostRequest(
      text = 'foo',
      inReplyTo = 'test-post-1',
    ),
  )


@then(u'My new post is created')
def step_impl(context):
  if context.try_type == 'Posts':
    assert isinstance(context.stubs.call_res, Post)
    context.new_post = context.stubs.call_res
  elif context.try_type == 'Conversations':
    assert hasattr(context.stubs.call_res, 'op')
    assert isinstance(context.stubs.call_res.op, Post)
    context.new_post = context.stubs.call_res.op


@then(u'The author display name is "{authorDisplayName}"')
def step_impl(context, authorDisplayName):
  assert context.new_post.authorDisplayName == authorDisplayName


@when(u'I make a new post')
def step_impl(context):
  req = CreatePostRequest(
    text = 'foo',
    inReplyTo = 'test-post-1',
  )
  if getattr(context, 'auth_user', None):
    req.authorDisplayName = context.auth_user['displayName']
  context.try_type = 'Posts'
  context.stubs.try_call(context.stubs.posts.Create, req)


@when(u'I fetch all posts by {userId}')
def step_impl(context, userId):
  context.stubs.try_call(
    context.stubs.posts.PostsByUser,
    PostsByUserRequest(authorId = userId)
  )


@then(u'I get {num:d} posts')
def step_impl(context, num):
  posts = list(context.stubs.call_res)
  assert len(posts) == num, 'got {} posts'.format(len(posts))


@when(u'I fetch the thread from {postId} after {postId2}')
def step_impl(context, postId, postId2):
  context.stubs.try_call(
    context.stubs.posts.Thread,
    ThreadRequest(postId = postId, after = postId2),
  )


@when(u'I fetch the thread from {postId} since {timestamp}')
def step_impl(context, postId, timestamp):
  req = ThreadRequest(postId = postId)
  req.since.FromJsonString(timestamp)
  context.stubs.try_call(context.stubs.posts.Thread, req)


@when(u'I fetch the thread from {postId}')
def step_impl(context, postId):
  context.stubs.try_call(
    context.stubs.posts.Thread,
    ThreadRequest(postId = postId)
  )
