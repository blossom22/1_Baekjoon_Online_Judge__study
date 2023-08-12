# Baekjoon_BRONZE3_13484: Tarifa    

x = int(input())
n = int(input())
a = [int(input()) for _ in range(n)]
hap = x
for i in a:
    hap += (x-i)
print(hap)