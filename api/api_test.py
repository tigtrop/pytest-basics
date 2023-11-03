import requests

# config

headers = {'Content-Type': 'application/json', 'User-Agent': 'Python Learning Requests'}
baseUrl = 'http://api.mathjs.org/v4/'

# test 1 square

response = requests.get(baseUrl, headers=headers, params={'expr': '2^2'})

print(response.text)

# test 2 plus

response = requests.post(baseUrl, headers=headers, json={'expr': ['2+2', '2-2', '3*3', '3/3']})

# print(response.json())
print(response.text)