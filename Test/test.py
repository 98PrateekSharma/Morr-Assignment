import requests

path = "http://127.0.0.1:5000"

documentation = requests.get(path)

print(documentation.text)

allContacts = requests.get(path + '/contacts')

print(allContacts.text)
