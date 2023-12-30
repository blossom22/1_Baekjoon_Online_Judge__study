# Baekjoon_CLASS2_Silver4_11047: 동전 0
# 그리디 알고리즘 문제이다. 최대한 적은 coin의 개수를 쓰도록 동전가치 리스트(a)에서 역순으로 검사하자
import sys
n,k = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
coin = 0
for i in range(n-1,-1,-1):
    if k//a[i]>0:
        coin += (k//a[i])
        k = (k%a[i])
print(coin)