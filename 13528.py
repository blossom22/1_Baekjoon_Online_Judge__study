# Baekjoon_BRONZE3_13528: Grass Seed Inc.     

c = float(input())
l = int(input())
a = [list(map(float, input().split())) for _ in range(l)]
hap = 0
for i in range(l):
    hap += a[i][0]*a[i][1]*c 
print("{:.7f}".format(hap))