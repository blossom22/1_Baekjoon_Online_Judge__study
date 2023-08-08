# Baekjoon_BRONZE4_28352: 10!

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
    
n = int(input())
print(fac(n)//(7*24*3600))