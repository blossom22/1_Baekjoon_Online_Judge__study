# Baekjoon_CLASS0_5597: 과제 안 내신 분..?


a = [int(input()) for _ in range(28)]
b = [i for i in range(1,31) if i not in a]
print(*b,sep='\n')