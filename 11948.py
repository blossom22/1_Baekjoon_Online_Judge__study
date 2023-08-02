# Baekjoon_BRONZE4_11948: 과목선택       

a = [int(input()) for _ in range(6)]
data_1 = a[:4]
data_2 = a[4:]
data_1.remove(min(data_1))
data_2.remove(min(data_2))
print(sum(data_1) + sum(data_2))