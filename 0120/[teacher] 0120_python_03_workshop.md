## 1. List의 합 구하기

> 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오

------

```
list_sum([1, 2, 3, 4, 5]) #=> 15
```



```
numbers = [1, 2, 3, 4, 5]

def list_sum(numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum
    
print(list_sum(numbers))
15
```

## 2. Dictionary로 이루어진 List의 합 구하기

> Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오

------

```python
dict_list_sum([{'name':'kim','age': 12},
               {'name':'lee','age':4}]) #=> 16
```



```
ages=[{'name':'kim','age': 12},
               {'name':'lee','age':4}]

def list_sum(ages):
    total=0
    for age in ages:
        total+=age['age']
    return total
print(list_sum(ages))
16
```





## 3. 2차원 List의 전체 합 구하기

> 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

------

```
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) #=> 55
```

