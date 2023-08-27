# Baekjoon_BRONZE3_28288: Special Event  

import sys
n = int(sys.stdin.readline())
dic = {1:0, 2:0, 3:0, 4:0, 5:0}
for i in range(n):
    a = input()
    for j in range(5):
        if a[j]=='Y':
            dic[j+1]+=1
a = [k for k,v in dic.items() if max(dic.values())==v]
print(*a,sep=',')