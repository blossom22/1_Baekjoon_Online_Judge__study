# Baekjoon_CLASS4_Gold2_1918: 후위 표기식

a = input()
operator = ["+", "-", "*", "/", "(", ")"]
stack = []
res = ""
for x in a:
    if x not in operator:
        res += x
    else:
        if x=="(":
            stack.append(x)
        elif x=="*" or x=="/":
            while stack and (stack[-1]=="*" or stack[-1]=="/"):
                res += stack.pop()
            stack.append(x)
        elif x=="+" or x=="-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x==")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)