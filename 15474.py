# Baekjoon_BRONZE4_15474: 鉛筆 (Pencils)  

import math
n,a,b,c,d = map(int, input().split())
set_a = math.ceil(n/a)*b
set_b = math.ceil(n/c)*d
print(min(set_a, set_b))