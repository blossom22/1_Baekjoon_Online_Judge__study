# Baekjoon_Silver3_15815: 천재 수학자 성필
# 간단한 후위표기식 연산문제였다 
n = input()
stack = []
for i in n:
    if i.isdecimal():
        stack.append(int(i))
    elif i=="+":
        n1=stack.pop()
        n2=stack.pop()
        stack.append(n2+n1)
    elif i=='-':
        n1=stack.pop()
        n2=stack.pop()
        stack.append(n2-n1)
    elif i=='*':
        n1=stack.pop()
        n2=stack.pop()
        stack.append(n2*n1)
    elif i=='/':
        n1=stack.pop()
        n2=stack.pop()
        stack.append(n2//n1)    # 문제조건에서 계산과정 중간의 모든 결과는 정수라고 했으므로 //사용
print(stack[0])