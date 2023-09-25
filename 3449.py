# Baekjoon_BRONZE2_3449: 해밍 거리 

t = int(input())
for i in range(t):
    a = input()
    b = input()
    c = len(a)
    cnt = 0
    for i in range(c):
        if a[i] != b[i]:
            cnt+=1
    print('Hamming distance is %d.' %cnt)

