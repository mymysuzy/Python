# a.sort().pop()이 불가능한 이유?



### (feat. return값에 신경써야 하는 이유)

```python
a=[3, 2, 1]

a.pop()
1

a.sort().pop()
==>> AttributeError 
#a.sort()의 return값이 None이기 때문에
#None.pop()을 실행할 수 없어서 에러가 난다.

sorted(a).pop()
3
# sorted(a)의 return값은 list기 때문에 .pop()이 실행가능하다.



# 이러한 이유 때문에 return값을 항상 신경써줘야 한다!

```



# 타입? 인스턴스? 클래스?

```python
class Person:
    pass

print(type(Person))
<class 'type'>
# Person의 타입은 type이다.

print(type(int))
<class 'type'>
# int의 타입은 type이다

# 결론
# 우리가 임의로 만든 클래스던(Person), 파이썬 내부에 정의된 클래스던(int)
# 타입은 type이다.
```

```python
sohyeon = Person()

print(type(sohyeon))
<class '__main__.Person'>
# sohyeon은 Person이라는 타입이다. 
# __main__은 파이썬 내부에서 출력하는 것으로 일단 신경쓰지말자.

print(type(Person))
<class 'type'>
```



## 반드시 init부분에 parameter를 전달해야 하나?



```python
class Furniture:
    def __init__(self): 
        return
        
    def desk(self, name):
        self.name=name
        return f'안녕, 나는 {self.name}'
    
# 이렇게 init 말고 다른 함수에 파라미터를 줄 수 있긴 하다

# 그러나 자바에서 객체를 만들면 클래스에 getter setter했던 것과 같이
# init부분에서 객체 만들자마자 초기화해주는 버릇을 들이자
```





## 인스턴스 호출

```python

Person클래스가 있다고 하였을 때,

IU = Person() # IU 인스턴스를 생성하고
IU.talk() # IU 가 말하도록 시키는 이 명령어가
Person.talk(IU) # 사실 파이썬 내부에선 이렇게 변환되어 실행되고 있던 것 이다.
```