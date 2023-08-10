# Baekjoon_BRONZE4_25191: 치킨댄스를 추는 곰곰이를 본 임스

n = int(input())
a,b = map(int, input().split())

juice = (a//2) + b
if juice<=n:
    print(juice)
else:
    print(n)