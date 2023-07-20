# Baekjoon_CLASS1_10809: 알파벳 찾기

from string import ascii_lowercase      # string 모듈의 ascii_lowercase를 import하여 리스트를 씌우면 편리하다
alpha = list(ascii_lowercase)
s = input()
a = [-1]*26
for i in range(len(s)):
    if s[i] in alpha:
        a[alpha.index(s[i])] = s.index(s[i])
print(*a)
