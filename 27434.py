# Baekjoon_BRONZE5_27434: 팩토리얼 3

n = int(input())
def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(fac(n))