import requests

name = input()

url =f'https://api.nationalize.io?name={name}'

print(url)

response = requests.get(url).json()

name = response['name']
country = response['country']

print(f'{name}의 예상국적은 {country[0]["probability"]}의 확률로 {country[0]["country_id"]}임둥~~')