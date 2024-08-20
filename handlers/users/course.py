# import requests
#
# URL = 'https://nbu.uz/uz/exchange-rates/json/'
#
# responses = requests.get(url=URL)
# data = responses.json()
# a = 'AUD'
# for i in data:
#     if i['code'] == a:
#         print(i['code'])
from tracemalloc import Trace
