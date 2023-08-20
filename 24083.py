# Baekjoon_BRONZE4_24083: 短針 (Hour Hand)

a = int(input())
b = int(input())
if (a+b)%12==0:
    print(12)
else:
    print((a+b)%12)