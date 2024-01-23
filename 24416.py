# Baekjoon_BRONZE1_24416: 알고리즘 수업 - 피보나치 수1
# 재귀로 풀면 시간초과가 나온다. 다이나믹 프로그래밍으로 해결해야한다 (이미 계산한 결과들을 메모리에 저장했다가 필요할때 꺼내쓰기)
import sys
n = int(sys.stdin.readline())
memo = [0] *(n+1)
def Dynamic(n):
    cnt = 0
    memo[1] = 1
    memo[2] = 1
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2]
        cnt += 1 
    return memo[n], cnt
print(*Dynamic(n))