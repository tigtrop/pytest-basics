import requests
import pytest

# config

headers = {'Content-Type': 'application/json', 'User-Agent': 'Python Learning Requests'}
baseUrl = 'http://api.mathjs.org/v4/'

# test 1 square
@pytest.mark.parametrize('number', [1, 2, 3, 4, 5])
def test_square(number):
    response = requests.get(baseUrl, headers=headers, params={'expr': number**2})

    assert int(response.text) == number*number

# test 2 plus
@pytest.mark.parametrize('number1, number2', [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])
def test_addition(number1, number2):
    response = requests.post(baseUrl, headers=headers, json={'expr': [str(number1)+ '+' +str(number2)]})
    answear = response.json()['result']
    assert  int(answear[0]) == number1+number2