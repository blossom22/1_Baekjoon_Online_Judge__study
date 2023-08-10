# Baekjoon_BRONZE4_13866: 팀 나누기  

a,b,c,d = map(int, input().split())
data = [a,b,c,d]
num_1 = min(data) + max(data)
data.remove(min(data))
data.remove(max(data))
num_2 = sum(data)
print(abs(num_1 - num_2))
