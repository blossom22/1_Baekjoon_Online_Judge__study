# Baekjoon_Silver3_29155: 개발자 지망생 구름이의 취업 뽀개기

import sys
ans = []
result = 0
n = int(sys.stdin.readline())
dif = list(map(int, sys.stdin.readline().split()))

q = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q.sort(key=lambda v:(v[0], v[1]))

# 아래는 풀어야하는 문제들만 구하는 과정이다.
mark = 0
i = 0
while True:
    try:
        if q[mark][0]==i+1:
            for j in range(dif[i]):
                ans.append(q[mark])
                mark+=1
            i+=1
        else:
            mark+=1
    except:
        break

# 아래는 점수를 구하는 과정이다. 
a = len(ans)
result += ans[0][1]     # 첫번째 값에 대해서는 미리 result에 더해줬다(아래에서 range(1,a)여서)
for i in range(1,a):
    if ans[i][0] == ans[i-1][0]:
        result += (ans[i][1]+(ans[i][1]-ans[i-1][1]))
    else:
        result += (ans[i][1] + 60)
print(result)