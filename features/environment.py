from reusable_code.url_gets import get_response
from behave import fixture
from config import base_url, city_id, api_key


@fixture
def triggerAPI(context):
    # SETUP useful for most of Test cases
    # This will pass the response Object of API between multiple Tests
    trigger_url = base_url + '?id=' + str(city_id) + '&appid=' + api_key
    context.response = get_response(trigger_url)
    yield context.response
    '''context is bdd parameter, which allows 
    passing of variable between 
    several Tests from fixture (inside environment file
    and for same bdd Test cases block: given when & then'''
