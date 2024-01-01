# Baekjoon_CLASS3_Silver3_2606: 바이러스

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

cnt = 0
def DFS(v, graph, ch, n):
    global cnt
    ch[v] = 1       # 탐색한 지역은 ch배열에서 1로 만들면서 재검색을 방지
    cnt += 1        # 1번과 연결된 컴퓨터들이 카운트될수록 1씩 cnt에 추가
    for nv in graph[v]:
        if ch[nv]==0:   # 검색을 하지 않았으면서, 1번노드에 연결된 점들이면 DFS함수를 재귀로 돌린다. 
            DFS(nv, graph, ch, n)

def solution(n, edge):
    global cnt
    ch = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for [a,b] in edge:
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    DFS(1, graph, ch, n)    # 1번 컴퓨터에서부터 시작한다. 
    return cnt-1    # 1번 컴퓨터를 제외한 나머지 컴퓨터들의 수만 구하면 된다. 

print(solution(n, edge))