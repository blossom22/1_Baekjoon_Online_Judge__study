# Baekjoon_BRONZE3_10817: 세 수

a,b,c = map(int, input().split())
ls = [a,b,c]
ls.remove(min(ls))
print(min(ls))
