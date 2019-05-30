import glob
import os
import grpc
import yaml
from client.post_pb2 import *
from client.post_pb2_grpc import PostsStub

class Stubs(object):
  def __init__(self, config):
    address = config.userdata.get('backend',
      os.environ.get('KITTENS_BACKEND',
      'localhost:50051'
      )
    )
    self.channel = grpc.insecure_channel(address)
    self.posts = PostsStub(self.channel)

def before_all(context):
  context.stubs = Stubs(context.config)
  context.contexts = {}
  context.active_contexts = []
  base = os.path.abspath(os.path.dirname(__file__) + '/../..')
  for fn in glob.glob('{}/specs/*.yaml'.format(base)):
    with open(fn) as f:
      data = yaml.load(f, yaml.Loader)
      for ctx in data.get('contexts', ()):
        context.contexts[ctx['name'].replace(' ', '-')] = ctx

def before_tag(context, tag):
  if tag.startswith('use-contexts.'):
    contexts = tag.split('.')[1:]
    for name in contexts:
      context.active_contexts.append(context.contexts[name])
