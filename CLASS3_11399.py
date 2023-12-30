# Baekjoon_CLASS3_Silver4_11399: ATM
# 돈을 인출하는데 적은 시간이 걸리는 사람부터 처리하면 된다. 
# 오름차순 정렬후, 가장 적은 시간이 걸리는 사람부터 더해나가자. 
import sys
n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
h.sort()
hap = 0
for i in range(1,n+1):
    hap += sum(h[:i])
print(hap)