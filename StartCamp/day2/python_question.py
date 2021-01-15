# 미니 실습2

import pprint

coin = {
    "BTC": { #일반적인 딕셔너리와는 다르게 키와 밸류의 밸류 안에 또 키와 밸류가 있다.
        "opening_price": "44405000",
        "closing_price": "38806000",
        "min_price": "36640000",
        "max_price": "44999000",
        "prev_closing_price": "44404000",
        "fluctate_24H": "-7463000",
        "fluctate_rate_24H": "-16.13"
    },
    "ETH": {
        "opening_price": "1458000",
        "closing_price": "1229000",
        "min_price": "1100000",
        "max_price": "1490000",
        "prev_closing_price": "1458000",
        "fluctate_24H": "-275000",
        "fluctate_rate_24H": "-18.28"
    },
    "XRP": {
        "opening_price": "364.5",
        "closing_price": "311.9",
        "min_price": "284.2",
        "max_price": "372.7",
        "prev_closing_price": "364.2",
        "fluctate_24H": "-90.6",
        "fluctate_rate_24H": "-22.51"
    }
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
# print(coin["BTC"].get("max_price"))
# print(coin["BTC"]["max_price"]) #원래 딕셔너리 구하듯이 이렇게 적어줘도 된다
#.get 사용시에는 [] 가 아니라 () 구나!
#.get("~~~")

#btc 의 opening price
# print(coin["BTC"]["opening_price"])
# a = coin["BTC"]["opening_price"]
# #xrp 의 opening price
# print(coin["XRP"]["opening_price"])
# b = coin["XRP"]["opening_price"]

# total = a + b
# #total opening price ?
# print(total)

# dictionary 를 그대로 출력하면 복잡해보임. 외장함수 하나 추천함. import pprint
# pprint.pprint(coin)

# pprint안에도 여러가지 기능이 있기 때문에 두번 적어줘야함 
# random.choice
# ramdon.sample 와 같이... 

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
# 형변환을 해줘야 한다...??


movie = {
    "movieInfo": {
        "movieNm": "광해, 왕이 된 남자",
        "movieNmEn": "Masquerade",
        "showTm": "131",
        "prdtYear": "2012",
        "openDt": "20120913",
        "typeNm": "장편",
        "nations": [
            {
            "nationNm": "한국"
            }
        ],
        "genres": [
            {
            "genreNm": "사극"
            },
            {
            "genreNm": "드라마"
            }
        ],
        "directors": [
            {
            "peopleNm": "추창민",
            "peopleNmEn": "CHOO Chang-min"
            }
        ],
        "actors": [
            {
            "peopleNm": "이병헌",
            "peopleNmEn": "LEE Byung-hun",
            "cast": "광해/하선"
            },
            {
            "peopleNm": "류승룡",
            "peopleNmEn": "RYU Seung-ryong",
            "cast": "허균"
            },
            {
            "peopleNm": "한효주",
            "peopleNmEn": "HAN Hyo-joo",
            "cast": "중전"
            }
        ]
    }
}

# 1. 영화의 제목을 출력하시오.
print(movie["movieInfo"]["movieNm"])

# 2. 다음 movie의 감독의 영어 이름을 출력하시오.
print(movie["movieInfo"]["directors"][0]['peopleNmEn'])
# directors가 리스트였다.
#{}를 []로 감싸는 모습은 리스트기 때문에.

# 3. 다음 movie의 배우의 인원을 출력하시오.
pprint.pprint(len(movie["movieInfo"]["actors"]))

#len() ==>> 갯수 세어주는 메서드 




# 조건문

n = 10
# 1. 주어진 양수 n이 홀수인지 짝수인지 판단해 출력하는 코드를 작성해라

if n % 2 == 0 :
    print('짝수')
else:
    print('홀수')

# 2. 주어진 숫자 n이 양수인지 0인지 음수인지 파단하여 출력하는 코드

# 반복문
# 1.
numbers = [1, 2, 3]

for number in numbers:
    print(number)

# 2. 
numbers = range(1, 10)
for number in numbers:
    if number % 2 ==1:
    print(f'숫자 {number}는 홀수네')