# Baekjoon_CLASS2_10814: 좌표 정렬하기
# 나이가 같은 경우 정렬되기 전의 인덱스값을 기준으로 배열한다고해서, 인덱스값을 따로 계산할 필요없다. 
# 그냥 아래처럼 sort하면, 나이순으로 정렬하고, 나이가 같으면 알아서 기존의 인덱스값대로 배치한다. 
import sys
n = int(sys.stdin.readline())
data = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda v:int(v[0]))
for i in data:
    print(int(i[0]), i[1])
