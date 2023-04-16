from behave import then
import json


@then(u'Current Temperature should be between "{lowest_possible_temp}" and "{higher_possible_temp}"')
def step_impl(context, lowest_possible_temp, higher_possible_temp):
    context.current_temp = json.loads(context.response.content)['list'][0]['main']['temp']
    ''' comment: above line will convert to python dict
    and then we extract temp from the array of predictions'''

    print('From json response extracted Current Temperature in Kelvin which is: ', context.current_temp)
    assert float(lowest_possible_temp) < context.current_temp < float(higher_possible_temp)


@then(u'feels like Temperature should be +-"{delta}" than Current temperature')
def step_impl(context, delta):
    context.feels_like_temp = json.loads(context.response.content)['list'][0]['main']['feels_like']
    print('From json response extracted Feels Like Temperature in Kelvin which is: ', context.feels_like_temp)
    assert context.current_temp-float(delta) < context.feels_like_temp < context.current_temp+float(delta)
