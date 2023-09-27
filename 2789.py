# Baekjoon_BRONZE2_2789: 유학 금지 

a = ['C','A','M','B','R','I','D','G','E']
n = list(input())
m = []
for i in n:
    if i not in a:
        m.append(i)
print(''.join(m))