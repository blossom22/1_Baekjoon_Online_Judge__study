# Baekjoon_BRONZE4_5534: 상근날드 

data = [int(input()) for _ in range(5)]
colaset = [data[i]+data[3]-50 for i in range(3)]
ciderset = [data[i]+data[4]-50 for i in range(3)]
print(min(min(colaset), min(ciderset)))