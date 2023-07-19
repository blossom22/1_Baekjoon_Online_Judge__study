# Baekjoon_CLASS1_2438: 별 찍기 - 1

n = int(input())
for i in range(1,n+1):
    print('*'*i)

# join함수를 써서 이런식으로도 가능하다. 
n = int(input())
print('\n'.join('*' * (i + 1) for i in range(n)))