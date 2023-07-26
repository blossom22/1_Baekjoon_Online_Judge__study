# Baekjoon_BRONZE4_4470: 줄번호  

n = int(input())
a = [input() for _ in range(n)]
for i in range(n):
    print('{0}. {1}'.format(i+1, a[i]))