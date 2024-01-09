# Baekjoon_Silver3_2910: 빈도 정렬

from collections import defaultdict
import sys, operator
n,c = map(int, sys.stdin.readline().split())
dic = defaultdict(int)
nl = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    dic[nl[i]] += 1
k = len(dic)
diclist = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

for i in range(k):
    for j in range(diclist[i][1]):
        print(diclist[i][0], end=' ')