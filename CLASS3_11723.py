# Baekjoon_CLASS3_Silver5_11723: 집합

import sys
m = int(sys.stdin.readline())
s = set()
for i in range(m):
    a = sys.stdin.readline().split()
    if a[0]=='add' and int(a[1]) not in s:
        s.add(int(a[1]))
    elif a[0]=='remove' and int(a[1]) in s:
        s.remove(int(a[1]))
    elif a[0]=='check':
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
    elif a[0]=='toggle':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.add(int(a[1]))
    elif a[0]=='all':
        s = set(range(1,21))
    elif a[0]=='empty':
        s = set()