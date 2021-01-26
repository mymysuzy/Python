# Homework

> 학습해야 할 내용

```
✓ 데이터 구조

✓ 메서드
```



## 1. 모음은 몇 개나 있을까?

문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오. 단, .count() 메서드를 활용하여 작성하시오.

```python
count_vowels('apple') #=> 2

count_vowels('banana') #=> 3
```

```
# 방법 1. 리스트를 따로 생성하여 
def count_vowels(words):
    vowels = 'aeiou'
    not_vowels=[]
    count=0
    for word in words:
        if word in vowels:
            not_vowels+=word
    return len(not_vowels)


count_vowels('banana')
```

```
# 방법 2. 오직 count로
def count_vowels(words):
    vowels = 'aeiou'
    count=0
    for word in words:
        if word in vowels:
            count+=1
    return count

count_vowels('apple')
```



## 2. 문자열 조작

다음 중, 문자열(string)을 조작하는 방법으로 옳지 않은 것을 고르시오

```
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.

(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list로 반환한다. 
    특정 문자를 지정하지 않으면 공백을 기준으로 나눈다.

(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다.

(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 
    특정 문자를 지정하지 않으면 오류가 발생한다.
```

(4) 번.

```
특정 문자를 지정할 경우엔 양쪽에서 해당 문자를 찾아 제거하는 것은 맞다. 

하지만 지정하지 않으면 좌우 모든 공백을 제거하기 때문에 오답이 된다.
```



## 3. 정사각형만 만들기

각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 only_square_area 함수를 작성하시오.

```python
only_square_area([32, 55, 63], [13, 32, 40, 55]) #=> [1024, 3025]
```

```
def only_square_area(numbers1,numbers2):
    total=[]
    for i in numbers1:
        for j in numbers2:
            if i == j:
                total.append(i**2)
    return total
            

        
only_square_area([32, 55, 63], [13, 32, 40, 55])
```

