# Homework

## 1. Built-in 함수

> Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

In [ ]:

```
abs
all
any
chr
dir
divmod
enumerate
eval
filter
hex
id
input
int
isinstance
len
list
map
max
min
oct
open
ord
pow
range
round
sorted
str
sum
tuple
type
zip
```

## 2. 정중앙 문자

> 문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

------

```python
get_middle_char('ssafy') #=> a
get_middle_char('coding') #=> di
```

In [22]:

```

def get_middle_char(words):
    if len(words)%2:
        length = len(words)//2
        word = words[length]
    else:
        length = len(words)//2
        word = words[length-1]+ words[length]
    return word

#get_middle_char('ssafy')

get_middle_char('coding')
```

Out[22]:

```
'di'
```



## 3. 위치 인자와 키워드 인자

> 다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는 코드를 고르시오.

------

```
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# 1.
ssafy('허준')

# 2.
ssafy(location='대전', name='철수')

# 3.
ssafy('영희', location='광주')

# 4.
ssafy(name = '길동', '구미')
```

In [ ]:

```
ssafy(name = '길동', '구미')
# ==>> 키워드 인자가 빠졌다.
```

## 4. 나의 반환값은

> 다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.

```python
def my_func(a,b):
    c=a+b
    print(c)
result = my_func(3, 7)
```

In [ ]:

```
함수 mu_func()를 사용하면 print(c)에 의해 result의 결과값은 10이 출력이되지만
함수 내에서 return이 되지 않았기 때문에
결과적으로 result에 저장된 값은 없다. # None
```

## 5. 가변 인자 리스트

> 가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정 수들의 평균 값을 반환하는 my_avg 함수를 작성하시오

```python
my_avg(77, 83, 95, 80, 70) #=> 81.0
```

In [25]:

```
def my_avg(*args):
    sum=0
    count=0
    for arg in args:
        sum+=arg
        count+=1
    return sum/count

my_avg(77, 83, 95, 80, 70)
```

Out[25]:

```
81.0
```