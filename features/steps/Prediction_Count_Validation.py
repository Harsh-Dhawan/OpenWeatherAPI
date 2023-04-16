from behave import when, then
import json


@when(u'We count number of predictions in response')
def step_impl(context):
    context.response = json.loads(context.response.content)  # conversion to python dict
    list = context.response['list']  # from API we get array of predictions for 3 days  hour prediction
    context.count = 0
    for _ in list:
        context.count+= 1
    print('No of Elements in the response is: ', context.count)



@then(u'Number of predictions should be 40')
def step_impl(context):
    assert context.count is 40    # validation
