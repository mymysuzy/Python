menu = ['예향정','착한통큰오리삼겹','장가계']
#print(menu)
#print(menu[0], menu[-1])

phone_book = {'예향정':'123-123', '착한통큰오리삼겹':'456-456', '장가계':'789-789'}
# print(phone_book)
# print(phone_book['장가계'])

import random

my_menu = random.choice(menu)
print(my_menu + '의 전번은'+ phone_book[my_menu]+'입니다')
print(f'{my_menu}의 전번은?')
