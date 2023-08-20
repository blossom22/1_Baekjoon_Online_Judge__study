# Baekjoon_BRONZE4_28519: 초콜릿 번갈아 먹기

n,m = map(int, input().split())
if n==m:
    print(n+m)
else:
    a = min(n,m)
    print(a+(a+1))