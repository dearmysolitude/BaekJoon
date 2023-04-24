
import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

distance = [1e9] * (N+1)
graph = [[] for _ in range (N+1)]  #
for _ in range(M):
    initial, destination, cost = map(int, input().split())
    graph[initial].append((destination, cost))

# print(graph)

start, end = map(int, input().split())

def dijkstra(begin):
    q = []
    heapq.heappush(q, (0, begin)) # 거리 / city 위치 쌍으로 입력된다
    distance[begin] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(start)
print(distance[end])