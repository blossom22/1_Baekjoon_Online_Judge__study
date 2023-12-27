# Baekjoon_Silver5_2535: 아시아 정보올림피아드

import sys
n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda v : -v[2])
cnt = 0
i = 0
nation = []     # 메달 수상자의 국가번호를 여기다가 추가시키고, 만약 같은 국가번호가 2개있으면 다음 사람으로 검색 넘어가게 한다. 
while cnt!=3:
    if nation.count(m[i][0])==2:
        i+=1
    else:
        nation.append(m[i][0])
        cnt+=1
        print(m[i][0], m[i][1])
        i+=1