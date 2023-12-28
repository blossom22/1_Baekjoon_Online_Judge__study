# Baekjoon_Silver5_2822: 점수 계산 

n = [int(input()) for _ in range(8)]
m = [[a+1,b] for a,b in enumerate(n)]
m.sort(key=lambda v: -v[1])
hap = 0
idx = []
for i in range(5):
    hap+=m[i][1]
    idx.append(m[i][0])
print(hap)
print(*sorted(idx))