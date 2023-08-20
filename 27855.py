# Baekjoon_BRONZE4_27855: Cornhole 

h1, b1 = map(int, input().split())
h2, b2 = map(int, input().split())
score1 = h1*3 + b1*1
score2 = h2*3 + b2*1
if score1 == score2:
    print('NO SCORE')
elif score1>score2:
    print(1, score1-score2)
else:
    print(2, score2-score1)