import sys
from collections import deque
input = sys.stdin.readline

city, edge, distance, fromwhere= map(int, input().split())
visited = [False] * (city+1)

edges = [[] for _ in range(city+1)]
for i in range(edge):
    a, b = map(int, input().split())
    edges[a].append(b)
distances = [0] * (city+1)


def bfs(start, k):
    visited[start] = True
    q = deque([start])
    distances[start] = 0
    ans = [] #여기에 None을 넣으면 값없이 하나의 인덱스 차지
    while q:
        now = q.popleft()
        for i in edges[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                distances[i] = distances[now] + 1
                if distances[i] == k:
                    ans.append(i)
    if len(ans) == 0:
        return [-1] ##
    else:
        ans.sort()
        return ans

Answer = bfs(fromwhere, distance)
print(*Answer, sep='\n')