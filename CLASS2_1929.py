# Baekjoon_CLASS2_1929: 소수 구하기

import sys
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

m, n = map(int, sys.stdin.readline().split())
for num in range(m, n + 1):
    if is_prime(num):
        print(num)


# 에라토스테네스의 체 알고리즘을 쓰는 방법은 더 효율적이다
'''
1. 소수를 판별할 범위를 정하고
2. 초기에는 모든 수를 소수로 가정하고, 소수 아닌 것을 제거해나간다(2부터 시작해서 2의 배수를 모두제거하고, 남은 수중 가장 작은 수를 다음 소수로 가정)
3. 남은 수 중에서 다음 소수의 배수를 모두 제거
4. 알고리즘 끝날때까지 남아있는 모든 수가 소수가 된다
'''
import sys

def sosu(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False   # 초기에 0,1은 소수가 아니므로 False 설정

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:                     # is_prime[i]가 True라며, i는 소수
            for j in range(i*i, n+1, i):    # i*i인 이유는 그보다 작은 배수들은 이미 그전단계에서 제거되어서
                is_prime[j] = False         # 배수들 전부 소수가 아니라고 출력

    return [num for num in range(n + 1) if is_prime[num]]   # 소수들을 리스트로 반환

m, n = map(int, sys.stdin.readline().split())

primes = sosu(n)
for num in primes:
    if num >= m:
        print(num)