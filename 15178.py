# Baekjoon_BRONZE3_15178: Angles  

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if sum(a[i]) == 180:
        print(*a[i], 'Seems OK')
    else:
        print(*a[i], 'Check')