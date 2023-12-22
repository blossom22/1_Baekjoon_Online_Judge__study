# Baekjoon_10546: 배부른 마라토너
# 완주자목록의 명단을 key값으로 참가자명단을 딕셔너리로 만든 dic에서 1씩 뺀다. 그랬을때 남는 1놈은 완주안한 놈
from collections import Counter
import sys
n = int(sys.stdin.readline())
# arr는 참가자명단, arr2는 완주자명단
arr = [sys.stdin.readline().strip('\n') for i in range(n)]
arr2 = [sys.stdin.readline().strip('\n') for i in range(n-1)]
dic = Counter(arr)
for i in arr2:
    dic[i]-=1
for key in dic:
    if dic[key]==1:
        print(key)
