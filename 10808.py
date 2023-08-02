# Baekjoon_BRONZE4_10808: 알파벳 개수  

from string import ascii_lowercase
a = list(ascii_lowercase)
num = [0]*26
n = input()
for i in n:
    num[a.index(i)] += 1
print(*num)