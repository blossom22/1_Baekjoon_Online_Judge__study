# Baekjoon_BRONZE2_2902: KMP는 왜 KMP일까? 

a = input().split('-')
b = []
for i in range(len(a)):
    b.append(a[i][0])
print(''.join(b))