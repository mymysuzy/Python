# Workshop

## 1. 평균 점수 구하기

key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.



```python
get_dict_avg({

'python':80,

'algotrithm':90,

'django':89,

'web':83
}) 
#=> 85.5
```

```python

def get_dict_avg(scores):
    result=[]

    for score in scores.values():
        result+=[score]

        
    return sum(result)/len(result)
    
get_dict_avg({

'python':80,

'algotrithm':90,

'django':89,

'web':83
}) 

```





## 2. 혈액형 분류하기

여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.

```python
count_blood([
    'A','B','A','O','AB',
    'O', 'A', 'B', 'O','B','AB'
]) 
#=> {'A':3, 'B':3, 'O':3, 'AB':3}
```

```python
def count_blood(blood_list):

    blood_dict = {}

    for blood in blood_list:
        if blood_dict.get(blood):
            blood_dict[blood] += 1  
        else:
            blood_dict[blood] = 1  
    return blood_dict

count_blood([
    'A','B','A','O','AB','AB',
    'O', 'A', 'B', 'O','B','AB'
]) 
```



### [참고] 딕셔너리에 Key, value값 넣는 방법

```python
my_dict={}

my_dict['a']=5

my_dict = {'a':5}
```