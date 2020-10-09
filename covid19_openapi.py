import requests
from pprint import pprint
from datetime import date, timedelta
import xmltodict
import json

def get_city_data():
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params ={
    'serviceKey' : 'RqB9rjsCp3atFbK5uSYWgKX5WebjPuz6HCxzjeOaMDKlhAI31STYHoYpuvgE4HN+MPTi/Tyzp7hJq8fQDwAaLA==',
    'pageNo': '1',
    'numOfRows' : '30',
    'startCreateDt' : '20201006',
    'endCreateDt' : '20201007',
    }
    res = requests.get(url, params=params)
    dict_data = xmltodict.parse(res.text)
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)
    return dict_data["response"]["body"]["items"]["item"]
