# Baekjoon_BRONZE3_11006: 남욱이의 닭장

t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    u = m*2-n
    t = m-u
    print(u,t)
