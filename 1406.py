# Baekjoon_Silver2_1406: 에디터 
# 커서에 집중하지 말자. 커서를 일일이 이동시키면 시간초과가 난다.
# 기존의 문자가 들어있는 스택1과 비어있는 스택2를 만들어서, 두 스택의 가운데에 커서가 고정되어있다고 생각하자.
# 그리고, 커서를 움직이는 것이 아니라 문자를 스택1과 스택2사이에서 이리저리 이동시키면서, 결과를 만들고, 두 스택을 합치면 끝
from collections import deque
import sys
stack1 = deque(sys.stdin.readline().strip())
stack2 = deque()
m = int(sys.stdin.readline())
dat = [sys.stdin.readline().strip() for _ in range(m)]

for i in range(m):
    # 커서가 왼쪽으로 가는 것은 곧 이동한 만큼의 stack1의 문자를 stack2에 appendleft하면 된다. 
    if dat[i]=='L' and stack1:
        stack2.appendleft(stack1.pop())
    # 커서가 오른쪽으로 가는 것은 곧 이동한 만큼의 stack2의 문자를 stack1에 append하면 된다. 
    elif dat[i]=='D' and stack2:
        stack1.append(stack2.popleft())
    elif dat[i]=='B' and stack1:
        stack1.pop()
    elif dat[i][0]=='P':
        stack1.append(dat[i][-1])
print(''.join(stack1+stack2))