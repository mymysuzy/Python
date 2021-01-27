# Practice 1

> 복잡한 자료구조의 (2차원 리스트) 반복문



## 복잡한 리스트의 합

> 2차원 리스트를 반복하는 방법을 알아봅시다.

- 주어진 아래의 리스트를 반복하여 숫자의 합을 반환하시오.

------

**예시 입력**

```python
numbers = [
    [1, 4],
    [10, 5],
    [20, 30]    
]
```

**예시 출력**

```python
sum_list([[1, 4], [10, 5], [20, 30]]) # 70
```



### 방법 1. - for 문을 활용하여 풀이하기

```python
for element in list:
```

```python
# 아래에 코드를 작성하세요.
def sum_list(numbers):
    sum=0
    for number in numbers:
        for i in number:
            sum+=i
    return sum
```

```python
print(sum_list([[1, 4], [10, 5], [20, 30]]))
70
```





### 방법 2. - Index로 접근하여 풀이하기

```python
for element in range(len(list)):

 * range(3) ==>> 0 ,1, 2
```



#### [참고] 보통 이중, 삼중 포문을 쓰게되면 이렇게 명명한다.

```
for i
    for j
        for k
```

```python
# 아래에 코드를 작성하세요.
def sum_list_index(numbers):
    result = 0
    
    # 외부 리스트를 (Index 값으로) 순회하여 내부 리스트를 하나씩 꺼낸다.
    for i in range(len(numbers)):  # range(3) -> 0, 1, 2
        # 내부 리스트를 (Index 값으로) 순회하여 숫자를 하나씩 꺼낸다.
        for j in range(len(numbers[i])):    # range(2) -> 0, 1
            # 최종 숫자 요소 접근 : 2차원_배열_이름[외부_리스트_인덱스][내부_리스트_인덱스]
            result += numbers[i][j]
    
    return result
```

```python
print(sum_list_index([[1, 4], [10, 5], [20, 30]]))
70
```





### 방법 3. - while 문을 활용하여 풀이하기

```python
while ____:
```

```python
## 아래에 코드를 작성하세요.
def sum_list_while(numbers):
    result = 0
    
    # 외부 리스트 순회
    i = 0  # 외부 리스트 인덱스값
    while i < len(numbers):  #=> 0, 1, 2
        # print(i)
        # print(numbers[i])
        
        # 내부 리스트 순회
        j = 0  # 내부 리스트 인덱스값
        while j < len(numbers[i]):  #=> 0, 1
            # 최종 숫자 요소 접근 : 2차원_배열_이름[외부_리스트_인덱스][내부_리스트_인덱스]
            result += numbers[i][j]
            # 내부 리스트의 다음 요소에 접근하기 위해 1 더하기
            j += 1
        # 외부 리스트의 다음 요소에 접근하기 위해 1 더하기
        i += 1
    
    return result
```

```python
print(sum_list_while([[1, 4], [10, 5], [20, 30]]))
70
```



## 시험 점수

> 2차원 배열

- A반 학생들의 점수는 아래와 같고, students 리스트에 저장되어 있다.
  - A학생(국어 100점, 수학 80점, 영어 100점)
  - B학생(국어 90점, 수학 90점, 영어 60점)
  - C학생(국어 80점, 수학 80점, 영어 80점)

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]
```

### (1) 학생별 출력

- 아래의 리스트를 반복하여 **학생별 총합**을 순서대로 `출력`하시오.
- `sum` 함수 사용 금지

------

**예시 입력**

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]
```

**예시 출력**

```python
280
240
240
```

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]
```

```python
def student_sum(students):
    

    row=0

    while row<len(students):
        i=0
        sum01=0
        for i in range(len(students[row])):
            sum01+=students[row][i]
            i+=1
        row+=1
        print(sum01)
student_sum(students)
280
240
240
```

```python
# 아래에 풀이를 작성하세요. 함수 정의는 필요없습니다.

for student in students:
    result = 0
    
    for score in student:
        result += score
    
    print(result)
280
240
240
```

```python
# for문 index 버전
def student_sum(students):
    for i in range(len(students)):  # i : 학생 리스트 인덱스
        print(students[i])
        result = 0

        for j in range(len(students[i])):  # j : 학생의 과목별 점수 리스트 인덱스
            result += students[i][j]  # 학생_데이터[학생_인덱스][학생의_과목_인덱스]

        print(result)
```



### (2) 과목별 출력

- 아래의 리스트를 반복하여 **과목별 총합**을 순서대로 `출력`하시오.
- `sum` 함수 사용 금지

------

**예시 입력**

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]
```

**예시 출력**

```python
270
250
240
```

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]
```

```python
def lecture_sum(students):

    row=0

    while row<len(students):
        i=0
        sum01=0
        for i in range(len(students[row])):
            sum01+=students[i][row]
            i+=1
        row+=1
        print(sum01)


lecture_sum(students)
270
250
240
```

```python
# IM 합격하기 위해 무수히 풀어볼 문제 유형
# 2중 for문을 순회하고,
# 2중 for문 안에서 내가 원하는 데이터만 적절하게 가져오기

# 우리가 원하는 데이터 (더해야 하는 데이터)
# 1) 점수_데이터[김지용][수학]
# 2) 점수_데이터[김보민][수학]
# 2) 점수_데이터[주원상][수학]


# 과목 : 0-국어, 1-수학, 2-영어
for x in range(len(students[0])):  
    
    # 과목별 점수 총합
    total = 0
    
    # 학생 : 0-김지용, 1-김보민, 2-주원상
    for y in range(len(students)):  
        
        # 김지용의 국어점수, 김보민 국어점수, 주원상의 국어점수
        total += students[y][x]
    
    # 과목별 점수 Print
    print(total)
270
250
240
```