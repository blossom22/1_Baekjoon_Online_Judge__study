# Baekjoon_BRONZE4_25238: 가희와 방어율 무시

from decimal import Decimal
a,b = map(int, input().split())
bang = Decimal(a*((100-b)/100))
print(1) if bang<100 else print(0)