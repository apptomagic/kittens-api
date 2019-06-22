import glob
import json
import os
import grpc
import yaml
from behave import *
from client import post_pb2
from client.post_pb2_grpc import PostsStub
from client import conversation_pb2
from client.conversation_pb2_grpc import ConversationsStub
from client import topic_pb2
from client.topic_pb2_grpc import TopicsStub

class Stubs(object):
  def __init__(self, context):
    self.context = context
    address = context.config.userdata.get('backend',
      os.environ.get('KITTENS_BACKEND',
      'localhost:50051'
      )
    )
    self.channel = grpc.insecure_channel(address)
    self.posts = PostsStub(self.channel)
    self.conversations = ConversationsStub(self.channel)
    self.topics = TopicsStub(self.channel)

  def try_call(self, call, *args, catch_error=False):
    metadata = []
    self.call_exc = self.call_res = None
    # print('using contexts:', [ctx['name'] for ctx in self.context.active_contexts[-1]])
    if self.context.active_contexts[-1]:
      metadata.append((
        'use-data-contexts',
        '+'.join(ctx['name'] for ctx in self.context.active_contexts[-1])
        ))
    user = getattr(self.context, 'auth_user', None)
    if user:
      metadata.append((
        'authenticated-user',
        json.dumps(user)
      ))
    try:
      self.call_res = call(*args, metadata=metadata)
    except grpc.RpcError as e:
      if catch_error:
        self.call_exc = e
      else:
        raise e

def before_all(context):
  context.stubs = Stubs(context)
  context.contexts = {}
  context.active_contexts = [[]]
  base = os.path.abspath(os.path.dirname(__file__) + '/../..')
  for fn in glob.glob('{}/specs/*.yaml'.format(base)):
    with open(fn) as f:
      data = yaml.load(f, yaml.Loader)
      for ctx in data.get('contexts', ()):
        context.contexts[ctx['name'].replace(' ', '-')] = ctx
        if 'posts' in ctx['data']:
          posts = []
          for data in ctx['data']['posts']:
            post = post_pb2.Post(
              id = data['id'],
              text = data['text'],
              authorId = data['authorId'],
              authorDisplayName = data['authorDisplayName'],
              conversationId = data.get('conversationId'),
              inReplyTo = data.get('inReplyTo')
            )
            if 'created' in data:
              post.created.FromJsonString(data['created'])
            if 'updated' in data:
              post.updated.FromJsonString(data['updated'])
            posts.append(post)
          context.stubs.posts.SetupContext(post_pb2.SetupContextRequest(
            name = ctx['name'],
            posts = posts
          ))
        if 'conversations' in ctx['data']:
          conversations = []
          for data in ctx['data']['conversations']:
            conversation = conversation_pb2.Conversation(
              id = data['id'],
              title = data['title'],
              opId = data['opId'],
              topics = data['topics'],
            )
            conversations.append(conversation)
          context.stubs.conversations.SetupContext(conversation_pb2.SetupContextRequest(
            name = ctx['name'],
            conversations = conversations
          ))


@fixture
def context_activator(context, contexts):
  # print('pushing contexts:', [ctx['name'] for ctx in contexts])
  context.active_contexts.append(contexts)
  yield contexts
  # print('popping contexts:', [ctx['name'] for ctx in contexts])
  context.active_contexts.pop()


def before_tag(context, tag):
  if tag.startswith('use-contexts.'):
    contexts = [context.contexts[name] for name in tag.split('.')[1:]]
    use_fixture(context_activator, context, contexts)
