# Baekjoon_BRONZE4_19944: 뉴비의 기준은 뭘까?

n,m = map(int, input().split())
if m==1 or m==2:
    print('NEWBIE!')
elif n>=m>2:
    print('OLDBIE!')
else:
    print('TLE!')