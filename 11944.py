# Baekjoon_Bronze2_11944: NN

import sys
n,m = map(str, sys.stdin.readline().split())
ans = ""
cnt = 0
while cnt<int(n) and len(ans)<=int(m):
    ans += n
    cnt += 1
print(ans[:int(m)])
