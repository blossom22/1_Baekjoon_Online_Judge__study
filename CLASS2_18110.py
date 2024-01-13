# Baekjoon_CLASS2_Silver4_18110: solved.ac  
# n이 10만까지 가므로, 시간복잡도는 O(n**2)이면 안된다.
from collections import deque
import sys
n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]
s.sort()
s = deque(s)
ans = 0
x = int(n*0.15+0.5)     # 그냥 round함수 쓰면 문제가 생긴다.
# 파이썬에서 반올림은 반올림하려는 수가 올림, 내림했을때 동일한 차이(0.5, 2.5...같은 수)를 갖는 경우, 짝수값으로 반올림한다. 
# 그래서 0.5를 round로 감싸면 0이된다. 이런 문제를 해결하려면, 나온 소수값에 0.5를 더해서 int()로 감싸서 소수점버림을 하면 된다.

for i in range(x):
    s.popleft()
    s.pop()
if n!=0:
    ans = int(sum(s)/(n-(x*2)) + 0.5)
    print(ans)
else:
    print(ans)
