# Baekjoon_CLASS0_10430: 나머지

import sys
a,b,c = map(int, sys.stdin.readline().split())
print((a+b)%c, ((a%c) + (b%c))%c, (a*b)%c, ((a%c) * (b%c))%c, sep='\n')