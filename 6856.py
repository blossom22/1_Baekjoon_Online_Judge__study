# Baekjoon_BRONZE3_6856: Roll the Dice  

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cnt = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if i+j == 10:
            cnt += 1
if cnt>1:
    print('There are {} ways to get the sum 10.'.format(cnt))
elif cnt==1:
    print('There is {} way to get the sum 10.'.format(cnt))
else:
    print('There are {} ways to get the sum 10.'.format(cnt))
