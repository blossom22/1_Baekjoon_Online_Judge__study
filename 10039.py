# Baekjoon_BRONZE4_10039: 평균 점수    
a = [int(input()) for _ in range(5)]
for i in range(5):
    if a[i]<40:
        a[i]=40
print(sum(a)//5)