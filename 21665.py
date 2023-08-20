# Baekjoon_BRONZE4_21665: Миша и негатив 

n,m = map(int, input().split())
first = []
second = []
for _ in range(n):
    first.extend([list(input())])
input()
for _ in range(n):
    second.extend([list(input())])
num = 0
for i in range(n):
    for j in range(m):
        if first[i][j] == second[i][j]:
            num += 1
print(num)