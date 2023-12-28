# Baekjoon_CLASS2_1920: 수 찾기 

import sys
n = int(sys.stdin.readline())
nset = set(map(int, sys.stdin.readline().split()))      # n개의 정수가 있는 이것은 굳이 중복값을 갖고 있을 필요가 없으니까 set으로 만든다.

m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))

for num in mlist:
    if num in nset:
        print(1)
    else:
        print(0)


# 이런식으로도 풀 수 있다.
import sys
n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()

m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))

answer = []
for i in mlist:
    left = 0
    right = len(nlist)-1
    while left<=right:
        mid = (left+right)//2
        if i==nlist[mid]:
            answer.append(1)
            break
        elif i>nlist[mid]:
            left = mid+1
        else:
            right = mid-1
    else:
        answer.append(0)
for i in answer:
    print(i)