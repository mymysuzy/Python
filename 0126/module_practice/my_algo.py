# 히히ㅣ히히

# 같은경로상
import check, random
print(check.odd(5))

print(dir(check))

# 다른경로상
# my_package안에 math 가 있다!
from my_package.math import tools

print(dir(tools))
print(tools.pi)

#shift+alrt+아래방향키 ==>> 복사
# 특정 함수나 변수만 사용하고 싶을 때 
from my_package.math.tools import pi, my_max
print(pi)
print(my_max(5,4))

# 애스터리스크 활용
from my_package.math.tools import *
print(pi)
print(my_max(5,4))

# as 를 사용하여 별명을 붙여준다. 충돌이 일어나지 않게 하기 위해!
from my_package.math.tools import pi as tools_pi
print(pi,tools_pi)



