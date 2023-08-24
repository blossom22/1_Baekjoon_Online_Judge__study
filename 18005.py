# Baekjoon_BRONZE3_18247: 겨울왕국 티켓 예매


t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    num = 1
    matrix = [[0]*m for _ in range(n)]
    for j in range(n):
        for k in range(m):
            matrix[j][k] = num
            num+=1
    try: 
        if matrix[11][3] != IndexError:
            print(matrix[11][3])
    except:
        print(-1)

