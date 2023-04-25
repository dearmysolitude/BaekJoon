import sys
import heapq

input = sys.stdin.readline

N = int(input())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
# print(N)
# print(maze)
# print(visited)
def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        changed, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            print(changed)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if maze[nx][ny] == 0: #까만 방이라면
                    heapq.heappush(q, (changed+1, nx, ny))
                else:
                    heapq.heappush(q, (changed, nx, ny))
dijkstra()