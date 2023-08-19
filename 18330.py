# Baekjoon_BRONZE4_18330: Petrol    

n = int(input())
k = int(input())

if n <= (60+k):
    print(n*1500)
else:
    print((60+k)*1500 + (n-(60+k))*3000)