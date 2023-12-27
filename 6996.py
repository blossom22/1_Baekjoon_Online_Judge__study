# Baekjoon_BRONZE1_6996: 애너그램 

from collections import Counter
n = int(input())
m = [list(map(str, input().split())) for _ in range(n)]
for i in range(n):
    if Counter(m[i][0])==Counter(m[i][1]):
        print('%s & %s are anagrams.'%(m[i][0], m[i][1]))
    else:
        print('%s & %s are NOT anagrams.'%(m[i][0], m[i][1]))
