# Baekjoon_CLASS2_BRONZE1_10989: 수 정렬하기 3

import sys
n = int(sys.stdin.readline())
arr = [0]*10001

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num]+=1
for i in range(10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)