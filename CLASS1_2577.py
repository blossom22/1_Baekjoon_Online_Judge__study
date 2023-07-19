# Baekjoon_CLASS1_2577: 숫자의 개수

import sys
a = 1
for _ in range(3):
    a *= int(sys.stdin.readline())      # 세 수를 곱한 것을 a에 저장
key_list = [0] * 10 
for i in str(a):
    key_list[int(i)] += 1
print(*key_list, sep='\n')