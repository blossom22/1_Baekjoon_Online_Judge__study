# Baekjoon_BRONZE3_6830: It’s Cold Here!

import sys
dic = {}
while True:
    n,m = map(str, sys.stdin.readline().split())
    if n != 'Waterloo':
        dic[n] = int(m)
    else:
        dic[n] = int(m)
        break
[print(i) for i,j in dic.items() if min(dic.values())==j]