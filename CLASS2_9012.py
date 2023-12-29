# Baekjoon_CLASS2_Silver4_9012: 괄호


def solution(v):
    stack = []
    for i in v:
        if i == ')':
            if len(stack)==0:
                return 'NO'
            stack.pop()
        else:
            stack.append(i)
    if len(stack)>0:
        return 'NO'
    return 'YES'

t = int(input())
for i in range(t):
    v = list(input())
    print(solution(v))