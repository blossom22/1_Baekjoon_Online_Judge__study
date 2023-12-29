# Baekjoon_Silver4_3986: 좋은 단어 
'''
문제 표현은 아치형곡선이 겹치네 마네라고 헷갈리게 말하는데, 
바꿔생각해보면 stack에서 다른 글자가 들어오면 append하고, 연속된 같은 글자가 들어오면 pop하여, 
최종적으로 빈 stack이 되면 '좋은 단어'가 되는 것이다. 
'''
n = int(input())
m = [input() for _ in range(n)]
cnt = 0
for i in m:
    stack = []
    for j in i:
        if len(stack)!=0 and stack[-1]==j:
            stack.pop()
        else:
            stack.append(j)
    if len(stack)==0:
        cnt+=1
print(cnt)