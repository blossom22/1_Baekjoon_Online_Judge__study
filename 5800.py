# Baekjoon_Silver5_5800: 성적 통계 

k = int(input())
for i in range(k):
    c = list(map(int, input().split()))
    n = c[0]
    del c[0]
    c.sort()
    minN = 0
    for j in range(len(c)-1):
        minN = max(minN, c[j+1]-c[j])
    print('Class %d' %(i+1))
    print('Max %d, Min %d, Largest gap %d' %(c[-1], c[0], minN))
