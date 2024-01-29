# Baekjoon_Silver3_17413: 단어 뒤집기 2

s = input()
stack = []
ans = ""
for i in s:
    if i.isalnum():
        stack.append(i)
    elif i.isspace() and ('<' not in stack) and ('>' not in stack):
        ans += ''.join(stack)[::-1]
        ans += ' '
        stack = []
    elif i.isspace():
        stack.append(i)
    elif i=='<' and not stack:
        stack.append(i)
    elif i=='<' and stack:
        ans += ''.join(stack)[::-1]
        stack = []
        stack.append(i)
    elif i=='>':
        stack.append(i)
        ans += ''.join(stack)
        stack = []
ans += ''.join(stack)[::-1] 
print(ans)