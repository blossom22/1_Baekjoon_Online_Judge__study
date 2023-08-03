# Baekjoon_BRONZE3_2576: 홀수

a = [int(input()) for _ in range(7)]
b = [i for i in a if i%2==1]
if len(b) == 0:
    print(-1)
else:
    print(sum(b), min(b), sep='\n')