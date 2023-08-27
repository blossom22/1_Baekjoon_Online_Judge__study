# Baekjoon_BRONZE3_14761: FizzBuzz 

import sys 
x,y,n = map(int, sys.stdin.readline().split())
for i in range(1,n+1):
    if i%x==0 and i%y==0:
        print('FizzBuzz')
    elif i%x==0:
        print('Fizz')
    elif i%y==0:
        print('Buzz')
    else:
        print(i)