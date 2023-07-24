# Baekjoon_CLASS0_2754: 학점계산

n = list(input())
score = {'-': 0, '0': 0.3, '+': 0.6}
def sosu(n):
    if n[1] in score:
        return round(a+score[n[1]],2)
if n[0] == 'A':
    a = 3.7
    print(sosu(n))
elif n[0] == 'B':
    a = 2.7
    print(sosu(n))
elif n[0] == 'C':
    a = 1.7
    print(sosu(n))
elif n[0] == 'D':
    a = 0.7
    print(sosu(n))
else:
    print(0.0)