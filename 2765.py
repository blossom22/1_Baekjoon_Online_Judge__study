# Baekjoon_Bronze3_2765: 자전거 속도

i = 1
while True:
    a,b,c = map(float, input().split())
    if b==0:
        break
    else:
        dist = a*3.1415927*b/12/5280
        mph = round(dist/(c/3600),2)
        dist = round(dist, 2)
        print(f"Trip #{i}: {dist:.2f} {mph:.2f}")
        i += 1