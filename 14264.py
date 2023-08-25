# Baekjoon_BRONZE3_14264: 정육각형과 삼각형 

import sys, math
l = int(sys.stdin.readline())
a = math.sqrt(3)/4*(l**2)
print('{:.10f}'.format((a*6 - 3*math.sqrt(3)/4*(l**2))/3))
