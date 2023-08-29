# Baekjoon_BRONZE3_10205: 헤라클레스와 히드라 

import sys
k = int(sys.stdin.readline())
for i in range(k):
    h = int(sys.stdin.readline())
    a = list(str(sys.stdin.readline()))
    for j in a:
        if j == 'c':
            h+=1
        elif j == 'b':
            h-=1
    print('Data Set {}:'.format(i+1))
    if h<=0:
        print(0)
    else:
        print(h)
    print()