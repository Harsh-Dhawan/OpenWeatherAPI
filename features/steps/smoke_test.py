from behave import then, use_fixture
from features.environment import triggerAPI
import json


@then(u'Response Code shall be 200')
def step_impl(context):
    context.response = use_fixture(triggerAPI, context)
    assert context.response.status_code is 200


@then(u'Response is not empty')
def step_impl(context):
    assert json.loads(context.response.content)['list'] is not None  # conversion to dict and extraction of tag
