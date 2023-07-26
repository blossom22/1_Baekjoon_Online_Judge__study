# Baekjoon_BRONZE1_1357: 뒤집힌 덧셈

import sys
x,y=map(int, sys.stdin.readline().split())
print(int(str(int(str(x)[::-1])+int(str(y)[::-1]))[::-1]))