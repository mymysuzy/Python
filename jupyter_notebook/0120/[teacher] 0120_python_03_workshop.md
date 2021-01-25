# Workshop

## 1. List의 합 구하기

> 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오

------

```
list_sum([1, 2, 3, 4, 5]) #=> 15
```

In [5]:

```


def list_sum(numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum
    
my_total = list_sum([1, 2, 3, 4, 5])  #=> 15
print(my_total)
15
```

## 2. Dictionary로 이루어진 List의 합 구하기

> Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오

------

```python
dict_list_sum([{'name':'kim','age': 12},
               {'name':'lee','age':4}]) #=> 16
```

In [7]:

```


def dict_list_sum(students):
    total=0
    for student in students:
        total+=student['age']
    return total


dict_list_sum([
    { 'name': '지용', 'age': 80 },
    { 'name': '원상', 'age': 37 },
])
```

Out[7]:

```
117
```

In [9]:

```
 # 2. 
    
def all_list_sum(number_lists):
    total = 0
    # 리스트 안의 리스트 순회 (-> [7, 8, 9, 10])
    for number_list in number_lists:  
        # 리스트 안의 리스트 안에 있는 숫자 순회 (-> 7, ..., 10)
        for number in number_list:   
            total += number
    return total

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])  #=> 55
```

Out[9]:

```
55
```



## 3. 2차원 List의 전체 합 구하기

> 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

------

```
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) #=> 55
```

In [4]:

```
number_lists = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

def all_list_sum(number_lists):
    total = 0
    for number_list in number_lists:
        for number in number_list:
            total+=number
        return total
    
print(all_list_sum(total))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-023f8b082acf> in <module>
      8         return total
      9 
---> 10 print(all_list_sum(total))

NameError: name 'total' is not defined
```


