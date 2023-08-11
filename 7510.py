# Baekjoon_BRONZE3_7510: 고급 수학   

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
for i in range(1,n+1):
    data = sorted(m[i-1])
    if data[0]**2 + data[1]**2 == data[2]**2:
        print('Scenario #{}:'.format(i), 'yes', sep='\n')
        print()
    else:
        print('Scenario #{}:'.format(i), 'no', sep='\n')
        print()
