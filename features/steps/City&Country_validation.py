from behave import given, then, use_fixture
from features.environment import triggerAPI
import json


@given(u'OpenWeatherAPI response')
def step_impl(context):
    context.response = use_fixture(triggerAPI, context)
    '''we will get response object from context, 
    this given block defined here is used at several places'''


@then(u'City Name should be "{city}"')
def step_impl(context, city):
    context.response = json.loads(context.response.content)  # we will create dict out of requests.response
    city_in_response = context.response['city']['name']  # way to extract data from python dict
    print('City in json response is: ', city_in_response)
    print('Expected City for test is: ', city)
    assert city == city_in_response # validation for city name


@then(u'Country code is "{country}"')
def step_impl(context, country):
    country_in_response = context.response['city']['country']
    print('Country in json response is: ', country_in_response)
    print('Expected Country for test is: ', country)
    assert country == country_in_response
