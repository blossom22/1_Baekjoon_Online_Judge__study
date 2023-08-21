# Baekjoon_BRONZE3_21312: 홀짝 칵테일 

a,b,c = map(int, input().split())
k = [a,b,c,a*b,a*c,b*c,a*b*c]
a = [a,b,c,a*b,a*c,b*c,a*b*c]

for i in range(7):
    if max(k)%2 == 1:
        print(max(k))
        break
    else:
        k.remove(max(k))
        if len(k)==0:
            print(max(a))
            break
