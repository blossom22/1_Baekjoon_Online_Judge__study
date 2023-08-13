# Baekjoon_BRONZE3_9085: 더하기 

t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    answer.append(sum(a))
print(*answer, sep='\n')