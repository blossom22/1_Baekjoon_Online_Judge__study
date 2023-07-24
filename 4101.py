# Baekjoon_CLASS0_4101: 크냐?

import sys
while True:
    a,b = map(int, sys.stdin.readline().split())
    if a !=0 or b !=0:
        if a>b:
            print('Yes')
        else:
            print('No')
    else:
        break