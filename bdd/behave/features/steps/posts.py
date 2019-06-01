# pylint: disable=function-redefined,no-name-in-module
from behave import given, when, then
import grpc
from client.post_pb2 import *

@when(u'I make a new post with no title and which is not a reply')
def step_impl(context):
  context.stubs.try_call(
    context.stubs.posts.Create,
    CreatePostRequest(text = 'foo'),
    catch_error = True,
  )


@then(u'It fails, telling me I must provide more data')
def step_impl(context):
  assert hasattr(context.stubs, 'call_exc')
  assert context.stubs.call_exc.code() == grpc.StatusCode.INVALID_ARGUMENT
  assert context.stubs.call_exc.details() == "Replies need inReplyTo, OPs need conversationId"


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
  assert isinstance(context.stubs.call_res, Post)


@then(u'The author display name is "{authorDisplayName}"')
def step_impl(context, authorDisplayName):
  assert context.stubs.call_res.authorDisplayName == authorDisplayName


@given(u'I\'m authenticated as {userId}')
def step_impl(context, userId):
  for ctx in context.active_contexts[-1]:
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
  context.stubs.try_call(
    context.stubs.posts.Create,
    CreatePostRequest(
      text = 'foo',
      authorDisplayName = context.auth_user['displayName'],
      inReplyTo = 'test-post-1',
    ))


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
