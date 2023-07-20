# Baekjoon_CLASS2_2609: 최대공약수와 최소공배수

import sys 
def mama(a,b):
    if b == 0:
        return a
    return mama(b,a%b)
def papa(a,b):
    result = (a*b)//mama(a,b)
    return result
a,b = map(int, sys.stdin.readline().split())
print(mama(a,b), papa(a,b), sep='\n')
