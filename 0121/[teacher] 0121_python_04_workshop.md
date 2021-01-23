## 1. 숫자의 의미

정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

> get_secret_word([83, 115, 65, 102, 89]) # => 'SsAfY'



```
# 아스키 코드 -> 문자
def get_secret_word(numbers):
    # 1. 변수 초기화
    word = ''
    
    # 2. numbers 순회
    for number in numbers:
        # 3. 문자로 변환해서 word에 붙이기
        word += chr(number)
    
    return word


get_secret_word([83, 115, 65, 102, 89]) #=> 'SsAfY'
```

```
'SsAfY'
```



## 2. 내 이름은 몇일까?

문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~~Z, a~~z로만 구성되어 있다.

> get_secret_number('tom') #=> 336



```
# 문자 -> 아스키 코드
def get_secret_number(word):
    total = 0
    
    for char in word:
        total += ord(char)
    
    return total


get_secret_number('tom') #=> 336
```

```
336
```



## 3. 강한 이름

문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하 여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

> get_strong_word('z', 'a') #=> 'z'

> get_strong_word('tom','john') #=> 'john'



```
# 아스키 코드로 대결하기
def get_strong_word(word1, word2):
    # word1 = 'tom'
    # word2 = 'john'
    
    word1_total = get_secret_number(word1)
    word2_total = get_secret_number(word2)
    
    if word1_total > word2_total:
        return word1
    else:
        return word2


print(get_strong_word('z', 'a')) #=> 'z'
print(get_strong_word('tom', 'john')) #=> 'john'
print(get_strong_word('bomin', 'sohyun')) #=> 'john'
print(get_strong_word('jiyong', 'sohyun')) #=> 'john'
z
john
sohyun
sohyun
```