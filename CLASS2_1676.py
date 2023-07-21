# Baekjoon_CLASS2_1676: 팩토리얼 0의 개수 

def fac(n):
    if n>1:
        return n*fac(n-1)
    else:
        return 1
n = int(input())
num = str(fac(n))
a = 0
for i in range(len(num)-1,-1,-1):
    if num[i] == '0':
        a+=1
    else:
        break
print(a)