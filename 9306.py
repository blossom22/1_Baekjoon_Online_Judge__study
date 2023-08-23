# Baekjoon_BRONZE3_9306: Practice: Roll Call

n = int(input())
case = []
for _ in range(n):
    f = input()
    l = input()
    case.append([l,f])
for i in range(n):
    print('Case {}: {}, {}'.format(i+1, case[i][0], case[i][1]))