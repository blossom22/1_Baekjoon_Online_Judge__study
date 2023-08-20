# Baekjoon_BRONZE3_3009: 네 번째 점  

a = [list(map(int, input().split())) for _ in range(3)]
xl = [a[i][0] for i in range(3)]
yl = [a[i][1] for i in range(3)]
x = 0
y = 0
for i in range(3):
    if xl.count(a[i][0]) == 1:
        x = a[i][0]
    if yl.count(a[i][1]) == 1:
        y = a[i][1]
print(x, y)
