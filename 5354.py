# Baekjoon_BRONZE3_5354: J박스 

t = int(input())
a = [int(input()) for _ in range(t)]

for i in range(t):
    if a[i]>2:
        side = '#'*a[i]
        mid = '#'+'J'*(a[i]-2)+'#'
        print(side)
        for j in range(a[i]-2):
            print(mid)
        print(side)
        print()
    elif a[i]<=2:
        for j in range(a[i]):
            print('#'*a[i])
        print()