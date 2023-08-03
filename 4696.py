# Baekjoon_BRONZE4_4696: St. Ives   

def multi(a):
    return a**4 + a**3 + a**2 + a + 1
while True:
    a = float(input())
    if a != 0:
        print("{:.2f}".format(multi(a)))
    else:
        break