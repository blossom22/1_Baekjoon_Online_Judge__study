# Baekjoon_Silver5_22403: 阿吽の呼吸 

def sol(n):
    stack = []
    w = [input() for i in range(n)]
    for i in w:
        if stack and stack[-1]=='A' and i=='Un':
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0:
        return 'YES'
    return 'NO'

n = int(input())
print(sol(n))
