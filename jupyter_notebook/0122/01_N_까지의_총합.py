'''
N 까지의 총합

정수 num을 기준으로, 1~num까지의 총 합을 구하는 함수를

1. `for` 문을 사용하여
2. `while`문을 사용하여

작성하시오.
'''

# for문만 사용하여 풀기
def sum_with_for(nums):
    sum=0
    for num in range(1,nums+1):
        sum+=num
    return sum
    

# while문만 사용하여 풀기
def sum_with_while(nums):
    sum=0
    count=1
    while count in range(1, nums+1):
        sum+=count
        count+=1
    return sum


# 아래 코드는 바꾸지 않습니다.
if __name__ == '__main__':
    print(sum_with_for(4))    # 10
    print(sum_with_while(4))  # 10
    print(sum_with_for(5))    # 15
    print(sum_with_while(5))  # 15