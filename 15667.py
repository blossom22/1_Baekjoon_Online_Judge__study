# Baekjoon_Bronze3_15667: 2018 연세대학교 프로그래밍 경진대회 
# 간단한 이차방정식 문제였다
import sys, math
n = int(sys.stdin.readline())
k = (-1+math.sqrt(4*n-3))/2
print(int(k))