menu = ['예향정','착한통큰오리삼겹','장가계']
phone_book = {'예향정':'123-123', '착한통큰오리삼겹':'456-456', '장가계':'789-789'}

import random

choiced_menu = random.choice(menu)

print(phone_book[choiced_menu])

print(f'{choiced_menu}의 전화번호는 {phone_book[choiced_menu]} 입니다. ')