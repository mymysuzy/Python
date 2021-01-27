# Practice 3

> 자료 구조



## 썩은 과일 찾기

> 과수원에 농부 한명이 썩은 과일이 몇개 들어있는 과일 봉지를 가지고 있다. (과일 봉지는 리스트를 의미한다.)
>
> 썩은 과일 조각들을 모두 신선한 것으로 교체하는 함수 `change_rotten_fruit()`를 작성하시오.
>
> 예를 들어,

- ```python
  ['apple', 'rottenBanana', 'apple']
  ```

   

  이라는 리스트가 주어진 경우, 대체된 리스트는

   

  ```python
  ['apple', 'banana', 'apple']
  ```

   

  이어야 한다.

  > **유의**

- 만약 리스트가 null/nil/None이거나 비어 있는 경우 빈 리스트를 반환한다.

- 반환된 리스트의 요소는 모두 소문자여야 한다.

------

예시)

```python
change_rotten_fruit(['apple', 'rottenBanana', 'apple']) 
#=> ['apple', 'banana', 'apple']

change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']) 
#=> ['apple', 'banana', 'apple', 'grape']
```

```python
# 새로운 리스트 만들어 풀기 - in 사용
def change_rotten_fruit(fruit_bag):
    new_bag = []
    for fruit in fruit_bag:
        if 'rotten' not in fruit:
            new_bag+=[fruit.lower()]
        else:
            new_bag+=[fruit[6:len(fruit)].lower()] # new_bag+=[fruit.lower()[6:len(fruit)]] 도 가능
            
    return new_bag

        
print(change_rotten_fruit(['Apple', 'rottenBanana', 'apple'] ))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))
['apple', 'banana', 'apple']
['apple', 'banana', 'apple', 'grape']
```

```python
# 새로운 리스트 만들어 풀기 - slicing 사용
def change_rotten_fruit(fruit_bag):
    new_fruit=[]
    for fruit in fruit_bag:
        if fruit[0:6] == 'rotten':
            new_fruit += [fruit.replace('rotten','').lower()]
        else:
            new_fruit+=[fruit]
    return new_fruit

        
print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))
['apple', 'banana', 'apple']
['apple', 'banana', 'apple', 'grape']
```

```python
# 교수님 풀이법. 새로운 리스트를 만들거나 하지 않고, 내용물을 바꾸고 원래의 글자에 다시 담는다.
def change_rotten_fruit(fruit_bag):
    result = []
    
    for fruit in fruit_bag:
        # 과일이 썩어있으면 신선한 것으로 바꾼다.
        # 1) rotten 문자를 지운다.
        fruit = fruit.replace('rotten', '')  # rottenBanana -> Banana
        # 2) 대문자를 소문자로 바꾼다. (B -> b)
        fruit = fruit.lower()  # Banana -> banana
        # 3. 바구니에 담는다.
        result.append(fruit)
    
    return result

# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))
['apple', 'banana', 'apple']
['apple', 'banana', 'apple', 'grape']
```



## 중복되지 않은 숫자의 합

> 같은 숫자가 한개 있거나 두개가 들어있는 리스트가 주어진다. 이러한 리스트에서 숫자가 한개만 있는 요소들의 합을 구하는 함수 `sum_of_repeat_number()`를 작성하시오.
>
> 예를 들어, `[4, 5, 7, 5, 4, 8]`는 7과 8이 한번만 나오기 때문에 두개를 더한 15가 결과값으로 도출된다.

------

예시)

```python
sum_of_repeat_number([4, 4, 7, 8, 10]) # => 25
```

```python
# 소현이 풀이
def sum_of_repeat_number(numbers):
    new_list=[]
    i=0
    for number in range(len(numbers)):
        if numbers.count(numbers[number]) == 1:
            new_list+=[numbers[number]]
    return sum(new_list)


print(sum_of_repeat_number([4, 4, 7, 8, 10]))
25
```

```python
# 여러번 등장한 숫자 리스트와 한 번만 등장한 숫자 리스트를 둘 다 구해보는 방법
def sum_of_repeat_number(numbers):
    once = []  # 한번 등장 리스트
    multiple = []  # 여러번 등장 리스트
    
    # 숫자 순회하면서 확인
    for number in numbers:
        # number가 한번 등장 리스트에 있으면 (== 두번째 등장)
        if number in once:
            multiple.append(number)  # 여러번 등장 리스트에 추가
            once.remove(number)  # 한번 등장 리스트에서 제거
        # number가 한번 등장 리스트에 없고 + 여러번 등장 리스트에도 없으면
        # (== 처음 등장)
        elif number not in multiple:
            once.append(number)
    
    # 처음 등장 리스트 숫자를 합해서 Return
    return sum(once)

print(sum_of_repeat_number([4, 4, 7, 8, 10]))
25
```

```python
# 리스트를 만들지 않고 구하는 방법
def sum_of_repeat_number(numbers):
    result = 0
    for number in numbers:
        if numbers.count(number) == 1:
            result += number
    return result

# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(sum_of_repeat_number([4, 4, 7, 8, 10]))
25
```

```python
# append를 사용하여 구하는 방법
def sum_of_repeat_number(numbers):
    sum_list=[]
    for number in numbers:
        if numbers.count(number) == 1:
            sum_list.append(number)
    return sum(sum_list)

# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(sum_of_repeat_number([4, 4, 7, 8, 10]))
            
25
```