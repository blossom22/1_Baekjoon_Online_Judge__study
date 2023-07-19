# Baekjoon_CLASS1_2884: 알람 시계 

h,m=map(int,input().split())
if m>=45:
    print(h, m-45)
else:
    if h-1<0:
        print(23, m+15)
    else:
        print(h-1, m+15)



# 아래는 시간을 전부 분으로 바꿔서 계산하는 방법이다. 
h, m = map(int, input().split())
total_minutes = h * 60 + m

# 45분을 빼고, 시간과 분으로 다시 분리
total_minutes -= 45
h = total_minutes // 60
m = total_minutes % 60

# 시간이 음수인 경우 23으로 처리
if h < 0:
    h = 23
print(h, m)