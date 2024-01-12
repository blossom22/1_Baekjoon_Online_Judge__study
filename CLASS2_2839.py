# Baekjoon_CLASS2_Silver4_2839: 설탕 배달

import sys
n = int(sys.stdin.readline())
bag = 1000000
a = n//5
b = n//3
cnt = 0
# 5kg봉지개수를 최대한 들때 기준으로 최소봉지개수 구한 코드
for i in range(a+1):
    if (n-5*i)%3==0:
        bag = min(bag, ((n-5*i)//3 + i))
    else:
        cnt += 1
# 3kg봉지개수를 최대한 들때 기준으로 최소봉지개수 구한 코드
for j in range(b+1):
    if (n-3*j)%5==0:
        bag = min(bag, ((n-3*j)//5 + j))
    else:
        cnt += 1
# 위의 두 과정을 거쳤는데, 3kg or 5kg봉지로 딱 맞춰 못가져오는 경우 -1출력
if cnt == (a+b+2):
    print(-1)
else:
    print(bag)