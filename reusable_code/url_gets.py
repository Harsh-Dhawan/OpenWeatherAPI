import requests

# url='https://api.openweathermap.org/data/2.5/forecast?id=5128581&appid=2976d3cc5649f3bf135824f4016e671d&units=metric'


def get_response(url):
    headers = {"Content-Type":"application/json"}
    response = requests.get(url, headers)
    response.encoding = 'utf8'
    return response