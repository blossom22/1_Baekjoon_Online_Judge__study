# Baekjoon_BRONZE2_28062: 준석이의 사탕 사기

import sys
n = int(sys.stdin.readline())
candy = list(map(int, sys.stdin.readline().split()))
odd = [i for i in candy if i%2==1]      # 홀수만 따로 모은다
hap = sum(candy)
while len(candy)>0:
    if hap%2==1:
        hap -= min(odd)     # 홀수개인 사탕묶음 중 가장 작은 홀수만 빼면 된다. 
        candy.remove(min(odd))
    else:
        print(hap)
        break
if len(candy)==0:
    print(0)