# Baekjoon_CLASS0_3733: Shares 
import sys
while True:
    try:
        a,b=map(int, sys.stdin.readline().split())
        print(b//(a+1))
    except:
        break