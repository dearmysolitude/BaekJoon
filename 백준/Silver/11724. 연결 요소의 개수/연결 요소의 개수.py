import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = [[False for _ in range(N+1)]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

visited = [False] * (N+1)

def dfs(i):
    if not visited[i]:
        visited[i] = True
        for j in range(1, N+1):
            if graph[i][j]==True:
                dfs(j)
    return

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)