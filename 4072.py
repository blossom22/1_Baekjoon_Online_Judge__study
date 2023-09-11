# Baekjoon_BRONZE2_4072: Words 

while True:
    a = input().split()
    if a != ['#']:
        for i in range(len(a)):
            print(a[i][::-1],end=' ')
        print()
    else:
        break