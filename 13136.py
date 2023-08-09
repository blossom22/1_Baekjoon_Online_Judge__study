# Baekjoon_BRONZE4_13136: Do Not Touch Anything

import math
r,c,n = map(int, input().split())
print(math.ceil(r/n) * math.ceil(c/n))