# Baekjoon_Silver5_5554: 반지

import sys
s = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]
cnt = 0
# 문자열을 데크에서의 rotate함수처럼 돌려주는 function을 만들었다.
def left_rotate(test_list, num):
    return test_list[num:] + test_list[:num]

for i in data:
    for j in range(10):
        if s in i:
            cnt += 1
            break
        else:
            i = left_rotate(i,1)
print(cnt)

