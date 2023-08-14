# Baekjoon_BRONZE4_28097: 모범생 포닉스  

n = int(input())
a = list(map(int, input().split()))
temp = (sum(a)+8*(len(a)-1))
print(temp//24, temp%24)