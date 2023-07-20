# Baekjoon_CLASS1_10871: X보다 작은 수

import sys
n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
[print(i,end=' ') for i in a if i<x]
