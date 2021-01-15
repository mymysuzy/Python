import requests

# 요청 url 확인 + 필요한 데이터 건네주기
name = input()
url = f'https://api.agify.io/?name={name}'

print(url)

# url로 요청보내기
response = requests.get(url).json()
# 우리는 제이슨이라는 데이터를 추출해야 하니 text가 아닌 .json()사용하여 제이슨덩어리로 바꿔보자

name = response['name']
age = response['age']
print(f'{name}의 예상나이는 {age}입니다.')