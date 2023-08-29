# Baekjoon_BRONZE3_10984: 내 학점을 구해줘     

t = int(input())
for i in range(t):
    n = int(input())
    hap = 0
    gpa = 0
    for j in range(n):
        a,b = map(float, input().split())
        hap += a
        gpa += a*b
    print(int(hap), '{:.1f}'.format(gpa/hap))