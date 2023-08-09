# Baekjoon_BRONZE4_23795: 사장님 도박은 재미로 하셔야 합니다

money = 0
while True:
    a = int(input())
    if a != -1:
        money += a
    else:
        print(money)
        break 