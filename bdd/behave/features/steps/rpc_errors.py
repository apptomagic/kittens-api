# pylint: disable=function-redefined,no-name-in-module
import grpc
from behave import given, when, then


@then(u'It fails, telling me I must provide more data')
def step_impl(context):
  assert hasattr(context.stubs, 'call_exc')
  assert context.stubs.call_exc.code() == grpc.StatusCode.INVALID_ARGUMENT
  assert context.stubs.call_exc.details().startswith(context.try_type + " need "), "Got error: " + context.stubs.call_exc.details()


@then(u'It fails, telling me I must provide {field}')
def step_impl(context, field):
  if field.startswith('a '):
    field = field[2:]
  elif field.startswith('an '):
    field = field[3:]
  assert hasattr(context.stubs, 'call_exc')
  assert context.stubs.call_exc.code() == grpc.StatusCode.INVALID_ARGUMENT
  assert context.stubs.call_exc.details() == context.try_type + " need " + field, "Got error: " + context.stubs.call_exc.details()
