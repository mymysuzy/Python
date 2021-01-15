number = 3
print(number)
print(type(number))

string = "문자" # 더블 쿼티션 안에 넣어주자
print(string)
print(type(string))

boolean = True
print(boolean)
print(type(boolean))

 #형변환

string_number = '3'
# #print(string_number+5) :: 에러남. 형이 서로 달라서.
print(int(string_number) + 5)

f-stirng

List
my_list = ['python','java', 'html',]
print(my_list[2],my_list)
my_list[2] = 'c'
print(my_list[2],my_list)

dictionary
dictionary 선언
age_dict = {
    '박소현':25,
    '김지용':27,
}
#리스트와 딕셔너리에 그 다음요소가 없음에도 불구하고
#콤마를 적는데 이를 trailing comma 라고 부르며
#중간에 리스트를 추가해야할 경우가 있는데 
# 그 때 마다 콤마를 추가하는 것을 까먹는 경우가 있어서
#미리 적어놓는것. 콤마를 미리 적어둔다 해서 에러 발생X

#dictionary 접근
print(age_dict['김지용'])
#혹은
print(age_dict.get('김지용'))

#dictionary 요소 변경
age_dict['김지용'] = 103
print(age_dict['김지용'])


