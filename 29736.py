# Baekjoon_BRONZE4_29736: 브실이와 친구가 되고 싶어 


import sys
a,b = map(int, sys.stdin.readline().split())
k,x = map(int, sys.stdin.readline().split())
f = 0
if k+x<a:
    print('IMPOSSIBLE')
elif k-x<=a and k+x<=b:
    print(k+x-a+1)
elif k-x<=a and k+x>b:
    print(b-a+1)
elif k-x>a and k+x<=b:
    print(k+x-(k-x)+1)
elif k-x>a and k+x>b:
    print(b-(k-x)+1)