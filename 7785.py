# Baekjoon_Silver5_7785: 회사에 있는 사람

import sys, operator
n = int(sys.stdin.readline())
dic = {}
for i in range(n):
    a,b = sys.stdin.readline().split()
    if b=='enter':
        dic[a] = 1
    else:
        dic[a] = 0
# operator모듈을 사용해서 딕셔너리의 key값을 기준으로 정렬시켰다 (내림차순을 물었으므로, reverse옵션도 추가)
for i,j in sorted(dic.items(), key=operator.itemgetter(0), reverse=True):
    if j==1:
        print(i)