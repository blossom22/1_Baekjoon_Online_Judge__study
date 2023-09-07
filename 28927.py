# Baekjoon_BRONZE5_28927: Киноманы 

import sys
t1, e1, f1 = map(int, sys.stdin.readline().split())
t2, e2, f2 = map(int, sys.stdin.readline().split())
a = t1*3 + e1*20 + f1*120
b = t2*3 + e2*20 + f2*120
print('Max') if a>b else print('Mel') if a<b else print('Draw')