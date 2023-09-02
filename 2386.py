# Baekjoon_BRONZE2_2386: 도비의 영어 공부   

while True:
    temp = input().lower()
    a = list(temp)
    if a[0] != '#':
        cnt = 0
        for i in a[2:]:
            if i == a[0]:
                cnt+=1
        print(a[0], cnt)
    else:
        break
