# Baekjoon_BRONZE3_6889: Smile with Similes 

n = int(input())
m = int(input())
adj = [input() for _ in range(n)]
noun = [input() for _ in range(m)]
for i in range(n):
    for j in range(m):
        print(adj[i], 'as', noun[j])