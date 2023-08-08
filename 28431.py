# Baekjoon_BRONZE4_28431: 양말 짝 맞추기  

a = [int(input()) for _ in range(5)]
for i in a:
    if a.count(i) == 1:
        print(i)
        break
    elif a.count(i) == 3:
        print(i)
        break
    elif a.count(i) == 5:
        print(i)
        break