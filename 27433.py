# Baekjoon_BRONZE5_27433: 팩토리얼 2

# 메모이제이션을 사용해서 풀어보았다. 재귀함수에 비해 훨씬 효율적이다.
n = int(input())
memo = {}
def fac(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        result = n * fac(n - 1)
        memo[n] = result
        return result
print(fac(n))