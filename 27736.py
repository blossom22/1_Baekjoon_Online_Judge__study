# Baekjoon_BRONZE3_27736: 찬반투표 

import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
if s.count(0)>=(n/2):
    print('INVALID')
elif s.count(1)>s.count(-1):
    print('APPROVED')
elif s.count(1)<=s.count(-1):
    print('REJECTED')