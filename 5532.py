# Baekjoon_BRONZE4_5532: 방학 숙제

import math
data = [int(input()) for _ in range(5)]
i = math.ceil(data[1]/data[3])      # math.ceil()은 소수점을 올림해서 정수로 표현한다
j = math.ceil(data[2]/data[4])
print(data[0] - max(i,j))