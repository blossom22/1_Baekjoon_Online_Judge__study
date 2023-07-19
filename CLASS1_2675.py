# Baekjoon_CLASS1_2675: 문자열 반복

t = int(input())
a = [input().split() for i in range(t)]
for i in range(t):
    for j in range(len(a[i][1])):
        print(a[i][1][j]*int(a[i][0]),end='')
    print()