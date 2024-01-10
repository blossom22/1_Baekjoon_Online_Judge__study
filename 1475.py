# Baekjoon_Silver5_1475: 방 번호


import sys
n = list(map(int, sys.stdin.readline().strip()))
arr = [0 for _ in range(9)]
for i in n:
    if i==6 or i==9:
        arr[6]+=1
    else:
        arr[i]+=1
maximum = max(arr)
# 아래의 res는 만약 maximum인 값이 여러개인지 체크하기 위한 리스트이다. filter함수를 사용했다
res = list(filter(lambda v:arr[v]==maximum, range(9)))

if len(res)==1 and arr[6]==maximum:
    if maximum%2==1:
        print(maximum//2 + 1)
    else:
        print(maximum//2)
else:
    print(maximum)