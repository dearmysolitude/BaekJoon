import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split())

tomatos = []
for h in range(H):
    tomatos.append([])
    for n in range(N):
        tomatos[h].append(list(map(int, input().split())))
 
def bfs():
    q = deque()

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatos[h][n][m] == 1:
                    q.append([m, n, h])

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]        

# 토마토 익히기
    while q:
        
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (0 <= nz < H and 0 <= ny < N and 0 <= nx < M and
                tomatos[nz][ny][nx] == 0):
                tomatos[nz][ny][nx] = tomatos[z][y][x]+1
                q.append([nx, ny, nz])
    day = 0
    for i in tomatos:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit(0)
            day = max(day, max(j))
    print(day-1)
bfs()