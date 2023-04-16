from reusable_code.url_gets import get_response
from behave import given, when, then
from config import base_url


@given(u'Base URL for OpenWeatherApi is provided')
def step_impl(context):
    context.url = base_url


@when(u'GET request is made with only 1 parameter "{parameter}" with value "{value}"')
def step_impl(context, parameter, value):
    url = context.url + '?' + parameter + '=' + value  # Adding parameters to URL for cityid & api
    print('making Get request with URL: ' + url)
    context.response = get_response(url)


@then(u'Status code should be "{error_code}"')
def step_impl(context, error_code):
    print('Get Request Code received: ', context.response.status_code)
    print('Get Request Response received: ' + context.response.text)
    print('Expecting Error Code: ' + error_code)
    assert context.response.status_code == int(error_code)
