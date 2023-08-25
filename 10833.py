# Baekjoon_BRONZE3_10833: 사과      

n = int(input())
cnt = 0
for i in range(n):
    s,a = map(int, input().split())
    cnt += a%s
print(cnt)