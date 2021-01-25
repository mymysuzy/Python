# Homework

> 데이터 & 제어문

## 1. mutable & immutable

제시 된 컨테이너들을 각각, 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

In [ ]:

```
# mutable
list, set, dictionary

# immutable
String, tuple, range()
```

## 2. 홀수 list

range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.

In [7]:

```
# 아래에 코드를 작성하시오.
numbers = list(range(51))
print(numbers[1::2])

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
```

## 3. dictionary 생성

반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

In [9]:

```
# 아래에 코드를 작성하시오.

middle_school = {'박소현':'28','박대전':'29','박구미':'30' }
print(middle_school)
{'박소현': '28', '박대전': '29', '박구미': '30'}
```

## 4. 반복문으로 네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

In [17]:

```
n = 5
m = 9

# 방법 1. 반복문 없이
print(('*'*n+'\n')*m)

# 방법 2. 반복문 이용
i = 1
while i <= m:
    print('*'*n)
    i+=1

*****
*****
*****
*****
*****
*****
*****
*****
*****

*****
*****
*****
*****
*****
*****
*****
*****
*****
```

## 5. 조건 표현식

제시된 if 문을 조건 표현식으로 바꾸어 작성하시오.

```python
temp = 36.5
if temp >= 37.5:
    print('입실 불가')
else:
    print('입실 가능')
```

In [19]:

```
temp = 36.5

print('입실 불가') if temp>=37.5 else print('입실가능')


입실 불가
```

## 6. list 평균값

제시된 list의 평균 값을 출력하시오.

In [8]:

```
scores = [80, 89, 99, 83]

# 아래에 코드를 작성하시오.
# print((scores[0]+scores[1]+scores[2]+scores[3])/4)

sum=0
for score in range(len(scores)):
    sum += scores[score]

average = sum / len(scores)

print(average)

87.75
```