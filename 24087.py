# Baekjoon_BRONZE4_24087: アイスクリーム (Ice Cream)

s = int(input())
a = int(input())
b = int(input())
price = 250
k = 0
while s>a+b*k:
    k+=1
    price+=100
print(price)