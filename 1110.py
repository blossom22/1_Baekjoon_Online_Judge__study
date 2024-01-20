# Baekjoon_BRONZE1_1110: 더하기 사이클

def makeStr(num):
    num = str(num)
    right_1 = num[-1]
    if len(num)<2:
        num = '0' + num
        right_2 = num[-1]
    else: 
        num = str(int(num[0])+int(num[1]))
        right_2 = num[-1]
    res = int(right_1 + right_2)
    return res

import sys
n = int(sys.stdin.readline())
tmp = 0
tmp = makeStr(n)
cnt = 1
while n!=tmp:
    tmp = makeStr(tmp)
    cnt += 1
print(cnt)