# Baekjoon_CLASS3_1764: 듣보잡
# defaultdict로 딕셔너리 제작후 문자열의 빈도수를 세서, 중복된 경우만 출력했다. 
from collections import defaultdict
n,m = map(int, input().split())
dic = defaultdict(int)
arr = [input() for _ in range(n+m)]
answer = []
for i in arr:
    dic[i]+=1
for key in dic:
    if dic[key]==2:
        answer.append(key)
print(len(answer))
for i in sorted(answer):
    print(i)
