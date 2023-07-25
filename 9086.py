# Baekjoon_CLASS0_9086: 문자열

n = int(input())
a = [input() for i in range(n)]
for i in range(n):
    print(a[i][0], a[i][-1], sep='')