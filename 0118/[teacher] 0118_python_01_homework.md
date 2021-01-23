### 1. python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하시오.

```python
and, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield
```

[참고1] 구지 외우지 않아도 아래의 코드로 찾을 수 있다.

```python
import keyword
print(keyword.kwlist)
```



[참고2] 예시로 print 를 변수로 사용해보았다.

```python
print = 'hi'
print(5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-33-2a55344b0a5d> in <module>
      2 # print은 이제 'hi'라는 값으로 인식되기 때문에 이전의 기능을 수행하지 못합니다.
      3 print = 'hi'
----> 4 print(5)

TypeError: 'str' object is not callable
```

==>> print는 이제 'hi'라는 값으로 인식되기 때문에 

​         이전의 기능을 수행할 수 없다...



### 2. 실수 비교

> python은 부동소수점 방식을 이용하여 실수(float)를 표현하는 과정에서, 나타내고자 하는 값과의 오차가 발생하여 원하는 대로 연산 또는 비교가 되지 않을 때가 있다. 
>
> 이를 참고하여, 아래와 같은 두 실수 값을 올바르게 비교하기 위한 코드를 작성하시오.
>
> num1 = 0.1*3
>
> num2= 0.3

```python
# 1. 기본적인 처리방법
abs(num1-num2) <= 1e-10
True

# 2. sys모듈 통해 처리하는 방법
# (epsilon은 부동소수점 연산에서 반올림을 함으로서 발생하는 오차 상환)
import sys
abs(num1 - num2) <= sys.float_info.epsilon
True

# 3. python 3.5부터 활용 가능한 math 모듈을 통해 처리
import math
math.isclose(num1,num2)
True
```





### 3. 이스케이프 시퀀스

> (1) 줄 바꿈, (2) 탭, (3) 백슬래시를 의미하는 이스케이프 시퀀스를 작성하시오.

``` python
# (1) 줄 바꿈 이스케이프 시퀀스 == \n
# (2) 탭 이스케이프 시퀀스 == \t
# (3) 백슬래시 이스케이프 시퀀스 == \\
```



### 4. String Interpolation

> “안녕, 철수야"를 string interpolation을 사용하여 출력하시오.

[참고] string interpolation == f-string

```python
print( f'안녕 {name}야')
```



### 5. 형 변환

> 다음 중, 실행 시 오류가 발생하는 코드를 고르시오.

```python
int('3.5') # int가 float 보다 표현할 수 있는 수의 범위가 작기 때문에 오류발생
		   # ValueError!
```

[참고] 

* bool 에서 True가 결과값인 이유는 

  bool에서는 0은 False 이며, 0이외의 나머지 숫자는 True기 때문이다.



### 6. 네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*)문자를 이용하여 출력하시오. 단, 반복문은 사용할 수 없다.

```python
n=5
m=9
print((n*'*'+'\n')*m)
```



### 7. 이스케이프 시퀀스 응용

print()함수를 한 번만 사용하여 다음 문장을 출력하시오.

> "파일은 c:\Windows\Users\내문서\Python에 저장이 되었습니다."
> 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'



```python
print(""" \"파일은 c:\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"
나는 생각했다. \'cd를 써서 git bash로 들어가봐야지.\'
""")
```



### 8. 근의 공식

```python
-b+(b**2-4*a*c)**0.5/(2*a) or -b-(b**2-4*a*c)**0.5/(2*a)
```

