# Baekjoon_Bronze2_1009: 분산처리

import sys
t = int(sys.stdin.readline())
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    tmp = []
    for i in range(1,b+1):
        if (a**i)%10 in tmp:
            break
        tmp.append((a**i)%10)
    if tmp[b%len(tmp)-1]==0:    # 일의자리수가 0인 것은 10으로 나눈 나머지가 없다는 뜻 = 10번컴퓨터가 처리해야함
        print(10)
    else:
        print(tmp[b%len(tmp)-1])