import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) # N은 사람의 수, M은 간선의 수
graph = [[] for _ in range(N+1) ] #인접 인덱스
indegree = [0 for _ in range(N+1)]
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) #a->b
    indegree[b] += 1

def topologySort():
    result = []    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

result = topologySort()
for i in result:
    print(i, end=' ')
print()