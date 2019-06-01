# pylint: disable=function-redefined,no-name-in-module
from behave import given, when, then


@given(u'I\'m not authenticated')
def step_impl(context):
  context.auth_user = None

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
