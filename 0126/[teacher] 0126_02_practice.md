# Practice 2

> 자료 구조



## 모든 위치

> 주어진 문자열(text)에서 제시된 알파벳(alphabet)의 등장 위치를 리스트로 반환하시오. 해당 알파벳이 등장하지 않으면, -1을 반환하시오.

------

예시)

```python
print(my_find('apple', 'p')) # [1, 2]
print(my_find('a', 'p'))     # -1
```

```python
def my_find(text, alphabet):
    cnt=[]
    for i in range(len(text)):
        if text[i] == alphabet:
            cnt+=[i]
    if cnt :
        return cnt
    return -1
    
    
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(my_find('apple', 'p'))
print(my_find('a', 'p'))



[1, 2]
-1
```

```python
def my_find(text, alphabet):
    # 제시된 알파벳이 주어진 문자열에 등장하지 않으면,
    if alphabet not in text:
        return -1
    
    # 제시된 알파벳이 주어진 문자열에 등장하면,
    result = []
    for i in range(len(text)):
        if text[i] == alphabet:
            result.append(i)
            
    # Pythonic!
    # for idx, char in enumerate(text):
    #    if char == alphabet:
    #        result.append(idx)
    
    return result
    
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(my_find('apple', 'p'))
print(my_find('a', 'p'))
```



## 출석 체크

> 주어진 학생 n과 출석한 학생명부 students 문자열이 있다. 결석한 학생들로 구성된 문자열을 반환하시오.
>
> n이 7일 때, 1 2 3 4 5 6 7의 출석 번호가 부여되고,
>
> '1 3 5'는 출석한 학생 명부이다.
>
> 즉, 결석한 학생 명부 '2 4 6 7'을 return 해야 한다.

------

예시)

```python
print(check(7, '1 3 5')) # 2 4 6 7
```

```python
# 전체에서 출석자들을 제외하는 방식
def check(n, students):
    students_list = list(map(int,students.split()))
    new_list=[]
    for i in range(1, n+1):
        new_list+=[i]
        
    for j in new_list:
        if j in students_list:
            new_list.remove(j)
    return new_list

```

```python
[1, 3, 5]
```

```python
def check(n, students):
    # 출석한 학생 : '1 3 5' -> [1, 3 5]
    students = list(map(int, students.split()))
    
    # 결석자 출석 번호 리스트
    absents = []
    
    # 1번부터 n번까지(전체 학생) 출석 번호 순회
    for i in range(1, n+1):
        # i번 학생이 출석한 학생 리스트에 없으면,
        if i not in students:
            # 결석자 리스트에 append
            absents.append(str(i))
    
    # '2 4 6 7' 문자열 형태로 Return
    return ' '.join(absents)
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(check(7, '1 3 5')) # 2 4 6 7
2 4 6 7
```