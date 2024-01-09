# Baekjoon_Silver5_1312: 소수
# 초딩때 나눗셈 처음 배울때 했듯이 나눗셈을 하면 된다. 
import sys
a,b,n = map(int, sys.stdin.readline().split())
ans = 0
for i in range(n+1):
    ans = a//b
    a = a%b*10
print(ans)