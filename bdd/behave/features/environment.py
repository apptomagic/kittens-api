import glob
import os
import grpc
import yaml
from behave import *
from client.post_pb2 import *
from client.post_pb2_grpc import PostsStub

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

  def try_call(self, call, *args, catch_error=False):
    metadata = []
    # print('using contexts:', [ctx['name'] for ctx in self.context.active_contexts[-1]])
    if self.context.active_contexts[-1]:
      metadata.append((
        'use-data-contexts',
        '+'.join(ctx['name'] for ctx in self.context.active_contexts[-1])
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
            post = Post(
              id = data['id'],
              text = data['text'],
              authorId = data['authorId'],
              authorDisplayName = data['authorDisplayName'],
              conversationTitle = data.get('conversationTitle'),
              inReplyTo = data.get('inReplyTo')
            )
            if 'created' in data:
              post.created.FromJsonString(data['created'])
            if 'updated' in data:
              post.updated.FromJsonString(data['updated'])
            posts.append(post)
          context.stubs.posts.SetupContext(SetupContextRequest(
            name = ctx['name'],
            posts = posts
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
