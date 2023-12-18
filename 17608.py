# Baekjoon_BRONZE2_17608: 막대기 
# 맨마지막 막대보다 크지만, 그보다 더 큰 막대가 오른쪽에 있어서, 가려질 수도 있다!
# 이 점을 고려해서, 막대들을 오른쪽에서부터 거꾸로 검색할때, 새로운 막대길이 최대값(temp)보다 큰 지 본다.
import sys
n = int(sys.stdin.readline())
stick = [int(sys.stdin.readline()) for i in range(n)]
a = 1
temp = stick[-1]
for i in range(n-2,-1,-1):
    if stick[i]>temp:
        temp = stick[i]
        a += 1
print(a)