# import requests
# url = 'http://ES_search_demo.com/'
# data = '''{
#   "query": {
#     "bool": {
#       "must": [
#         {
#           "text": {
#             "record.document": "SOME_JOURNAL"
#           }
#         },
#         {
#           "text": {
#             "record.articleTitle": "farmers"
#           }
#         }
#       ],
#       "must_not": [],
#       "should": []
#     }
#   },
#   "from": 0,
#   "size": 50,
#   "sort": [],
#   "facets": {}
# }'''
# response = requests.post(url, data=data)


import googlemaps
from datetime import datetime
import json


gmaps = googlemaps.Client(key='API KEY HERE ')

# now = datetime.now()
now = datetime.strptime('Aug 27 2019 7:33PM', '%b %d %Y %I:%M%p')
print(now)
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="driving",
                                     departure_time=now)

jsonResult = json.loads(json.dumps(directions_result[0]))

print(jsonResult["legs"][0]["duration"]["text"])

print(directions_result[0])
# print(jsonResult)
