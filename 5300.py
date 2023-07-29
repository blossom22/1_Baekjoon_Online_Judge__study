# Baekjoon_BRONZE4_5300: Fill the Rowboats!

n = int(input())
i = 1
while i<n+1:
    if i%6==0 or i==n:
        print(i, 'Go!', end=' ')
        i+=1
    else:
        print(i, end=' ')
        i+=1