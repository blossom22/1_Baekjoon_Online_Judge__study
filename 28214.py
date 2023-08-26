# Baekjoon_BRONZE3_28214: 크림빵     

n,k,p = map(int, input().split())
arr = list(map(int, input().split()))
cream = [arr[i:i+k] for i in range(0,n*k,k)]
cnt = 0
for i in range(n):
    if cream[i].count(0)<p:
        cnt+=1
print(cnt)