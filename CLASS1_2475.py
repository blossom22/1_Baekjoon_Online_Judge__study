# Baekjoon_CLASS1_2475: 검증수

import sys
a = list(map(int, sys.stdin.readline().split()))
print(sum([i**2 for i in a])%10)