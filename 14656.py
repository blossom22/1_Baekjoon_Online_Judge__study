# Baekjoon_BRONZE3_14656: 조교는 새디스트야!!   

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
answer = 0
for i in range(n):
    if a[i] != b[i]:
        answer += 1
print(answer)