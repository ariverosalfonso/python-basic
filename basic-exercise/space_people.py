import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print(json)

print('The people currently in the api are:')
for p in json['people']:
    print(p['name'])