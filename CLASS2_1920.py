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