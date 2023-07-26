# Baekjoon_BRONZE5_10872: 팩토리얼

n = int(input())
def fac(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*fac(n-1)
print(fac(n))