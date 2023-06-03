# 토마토
# 토마토가 익을때 까지의 최소 날짜는? 익어있다면 0, 익지 못하면 -1 출력

# 헷갈려서 다시 찾아봤다.........
import sys
from collections import deque
input = sys.stdin.readline

ans = 0
N, M = map(int, input().split())
tomatos = [] * M

for _ in range(M):
    tomatos.append(list(map(int, input().split())))

# print(tomatos[y][x]) 
def bfs(arr):
    q = deque()
    for i in range(M):
        for j in range(N):
            if(arr[i][j]==1):
                q.append([i,j])
    while q:
        y, x = q.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
        
            if (0 <= nx < N and 0 <= ny < M and arr[ny][nx] == 0):
                arr[ny][nx] = arr[y][x] + 1
                q.append([ny, nx])

bfs(tomatos)
for i in tomatos:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)