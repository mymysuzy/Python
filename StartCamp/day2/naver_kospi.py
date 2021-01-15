# 요청 보낼 주소 확인

url = 'https://finance.naver.com/sise/'

# request로 요청을 보내고 응답 txt 받기.

import requests

response = requests.get(url).text

# print(type(response))

#beautifulsoup :: 거대한 스트링을 구조화여 데이터추출하기 좋은 형태로 바꿔준다

from bs4 import BeautifulSoup

soup = BeautifulSoup(response, 'html.parser')
# parsing :: 데이터를 뽑아내서 분석한다
print(type(soup))

# 경로를 건네주고 원하는 정보 추출하기

# soup의 형태는 단순한 string형이 아닌 뷰티풀 수프의 형태임

kospi = soup.select_one('#KOSPI_now')
print(kospi)
#KOSPI_now 의 #의 의미는 유일한 값의의미다.

kospi = soup.select_one('#KOSPI_now').text
print(kospi)

print(f'현재 코스피 지수는 {kospi}입니다.')

import datetime
# 시간, 날짜기능을 도와주는 외장함수

now = datetime.datetime.now()
print(f'{now} 코스피 지수는 {kospi}입니다.')