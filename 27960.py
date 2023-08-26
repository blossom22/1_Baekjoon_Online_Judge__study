# Baekjoon_BRONZE3_27960: 사격 내기     

import sys
a,b = map(int, sys.stdin.readline().split())
dic = {1:0, 2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0, 512:0}
score = sorted(list(dic.keys()),reverse=True)
for i in score:
    if a//i>=1:
        dic[i]+=1
        a = a%i
    if b//i>=1:
        dic[i]+=1 
        b = b%i
c = 0
for i in score:
    if dic[i] == 1:
        c+=i
print(c)