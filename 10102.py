# Baekjoon_BRONZE3_10102: 개표     

v = int(input())
poll = list(input())
a = poll.count('A')
b = poll.count('B')
print('A') if a>b else print('B') if a<b else print('Tie')