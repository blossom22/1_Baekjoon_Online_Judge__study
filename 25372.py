# Baekjoon_BRONZE5_25372: 성택이의 은밀한 비밀번호     

import sys
n = int(sys.stdin.readline())
a = [input() for _ in range(n)]
[print('yes') if 6<=len(a[i])<=9 else print('no') for i in range(n)]