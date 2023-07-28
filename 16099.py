# Baekjoon_BRONZE5_16099: Larger Sport Facility   

import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
[print('TelecomParisTech') if a[i][0]*a[i][1]>a[i][2]*a[i][3] else print('Eurecom') if a[i][0]*a[i][1]<a[i][2]*a[i][3] else print('Tie') for i in range(n)]
