# 가장 최근에 메세지 보낸 사용자의 ID를 찾아서 안녕하세요 라고 메세지 보내기

# 요청에 필요한 라이브러리 인포트
import requests, pprint
# 요청 url 파악 및 secret한 api이면 토큰까지 알아낼 필요가 있다
token = '1516249307:AAHVIGT52mHDQuP-bo6bDgfPK5QP-7mVKv8'
api_url = f'https://api.telegram.org/bot{token}'

# 메세지 보낸 사용자의 ID값 찾기
chat_id_url = f'{api_url}/getUpdates'
response = requests.get(chat_id_url).json()
#pprint.pprint(response)
chat_id = response['result'][0]['message']['chat']['id']

print(chat_id)

# chat id 에게 메시지 보내기
text = input('메시지 입력하세요오오오오')
message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)