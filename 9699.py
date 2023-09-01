# Baekjoon_BRONZE3_9699: RICE SACK 

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    print('Case #{}: {}'.format(i+1, max(a)))