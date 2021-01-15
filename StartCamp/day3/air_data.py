import requests, pprint



# key 부분에는 일반 인증키 (UTF-8)가 들어간다.
key = ''
# url 부분에는 End point 값이 들어가며 제일 뒷 부분에 ?service={key}를 추가해 준다.
url = f''

response = requests.get(url).json()
# pprint.pprint(response)

sido_name = response['response']['body']['items'][1]['sidoName']
pm_10 = response['response']['body']['items'][1]['pm10Value']
station_name = response['response']['body']['items'][1]['stationName']

print(f'{sido_name}의 미세먼지 농도는 {pm_10}입니다. ( 측성소 : {station_name})')

# 텔레그램 메세지 전송

token = token = ''
chat_id = ''


telegram_url = f'https://api.telegram.org/bot/sendMessage?chat_id={chat_id}&text={text}'

requests.get(telegram_url)