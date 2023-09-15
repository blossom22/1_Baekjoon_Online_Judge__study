# Baekjoon_BRONZE5_29731: 2033년 밈 투표

n = int(input())
a = ['Never gonna give you up', 
    'Never gonna let you down', 
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
    ]
cnt = 0
c = 0
for _ in range(n):
    b = input()
    if b not in a:
        c+=1
    else:
        cnt+=1
if cnt==n:
    print('No')
elif c!=0:
    print('Yes')