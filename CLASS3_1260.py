# Baekjoon_CLASS3_Silver2_1260: DFS와 BFS

from collections import deque
import sys
n, m, v = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for [a,b] in edges:
    graph[a].append(b)
    graph[b].append(a)

# 아래 2개는 DFS방식(깊이우선탐색)
def DFS(v,ch,graph):
    global answer
    ch[v] = 1
    for nv in sorted(graph[v]):
        if ch[nv]==0:
            answer.append(nv)
            DFS(nv, ch, graph)
def DFS_sol(n,v,graph):
    global answer
    answer = []
    answer.append(v)
    ch = [0]*(n+1)
    DFS(v,ch,graph)
    return answer

# 아래는 BFS방식(너비우선탐색)
def BFS(n,v,graph):
    answer = []
    Q = deque()
    Q.append(v)
    ch = [0]*(n+1)
    ch[v] = 1
    while Q:
        tmp = len(Q)
        for i in range(tmp):
            x = Q.popleft()
            answer.append(x)
            for nx in sorted(graph[x]):
                if ch[nx]==0:
                    Q.append(nx)
                    ch[nx] = 1
    return answer

print(*DFS_sol(n,v,graph))
print(*BFS(n,v,graph))