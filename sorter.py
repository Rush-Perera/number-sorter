#import mongo client
from pymongo import MongoClient
import pandas as pd
import csv

client = MongoClient()  # Connect to the default MongoDB Server
db = client['rainbowpages']  # Get a database named 'rainbowpages'
collection = db['entertainment'] 

items = collection.find()
new_items = []
for item in items:
    try:
        item['Telephone'] = item['Telephone'].replace(' ', '')
        # split the numbers by comma and add them to a new array
        if ',' in item['Telephone']:
          temps = item['Telephone'].split(',')
          for temp in temps:
            new_items.append(temp)
        else:
          new_items.append(item['Telephone'])

    except KeyError:
        pass

with open('numbers-entertainment-mobitel.csv', 'w', newline='') as f:
  fieldnames = ['number']
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()

  for new_item in new_items:
      if new_item.startswith('071') or new_item.startswith('71') or new_item.startswith('070') or new_item.startswith('70'):
        print(new_item)
        writer.writerow({'number': new_item})

        