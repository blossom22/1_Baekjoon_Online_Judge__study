# Baekjoon_CLASS1_10950: A+B - 3

import sys
t = int(sys.stdin.readline())
a = [sum(list(map(int,sys.stdin.readline().split()))) for i in range(t)]
print(*a,sep='\n')
