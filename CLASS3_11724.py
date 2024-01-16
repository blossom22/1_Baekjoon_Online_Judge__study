# Baekjoon_CLASS3_Silver2_11724: 연결 요소의 개수

import sys
sys.setrecursionlimit(10 ** 6)      # 재귀깊이 제한을 설정하는 함수이다. RecursionError를 막아준다. (파이썬에서 재귀깊이 제한은 1000. 이를 10**6으로 늘려주는 것)
n,m = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

def DFS(v,graph,ch,n):
    ch[v] = 1
    for nv in graph[v]:
        if ch[nv]==0:
            DFS(nv, graph, ch, n)

def solution(n, edges):
    answer = 0
    ch = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for [u,v] in edges:
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,n+1):
        if ch[i]==0:
            answer += 1
            DFS(i, graph, ch, n)
    return answer
print(solution(n,edges))