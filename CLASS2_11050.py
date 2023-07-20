# Baekjoon_CLASS2_11050: 이항 계수1

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fac(n-1)
n, k = map(int, input().split())
a = fac(n)
b = fac(n - k)
c = fac(k)
print(a//(b * c))
