# Baekjoon_BRONZE3_10409: 서버   

n,t = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
for i in data:
    t -= i
    if t>=0:
        cnt += 1
print(cnt)