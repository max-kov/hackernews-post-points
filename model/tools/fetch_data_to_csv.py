import grequests
import requests
import json
import csv

api_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"
max_item = json.loads(requests.get("https://hacker-news.firebaseio.com/v0/maxitem.json").content)
csv_columns = ['by', 'id', 'score', 'url', 'title', 'time', 'type']
entries_to_fetch = 1000

request_urls = (grequests.get(api_url.format(i)) for i in range(max_item-entries_to_fetch, max_item))
responses = grequests.map(request_urls)

with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns, extrasaction='ignore')
    writer.writeheader()
    for response in responses:
        data = json.loads(response.content)
        writer.writerow(data)