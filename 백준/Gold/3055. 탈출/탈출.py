from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

woods = [list(input().strip()) for _ in range(n)]
time = [[0]*m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] ##왜 답안에서는 -랑 + 순서를 바꾸었을까
q = deque()

# bfs로의 탐색은 
def bfs(Dx, Dy):
    while q:
        x, y = q.popleft()
        if woods[Dx][Dy] == 'S': #해당 위치에 도착하면 걸린 시간을 반환
            return time[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (woods[nx][ny]=='.'or woods[nx][ny]=='D') and woods[x][y] == 'S': # 먼저 고슴도치가 갈 수 있는 곳을 가게 한다.
                    woods[nx][ny] = 'S'
                    time[nx][ny] = time[x][y] + 1 # 비버는 이전에 움직인 수+1만큼 움직인 것이 된다.
                    q.append((nx, ny))
                elif (woods[nx][ny] == '.' or woods[nx][ny] == 'S' and woods[x][y] == '*'): #나중에 물이 가게 하여 잘못된 곳에 간 고슴도치는 덮어씌워진다
                    woods[nx][ny] = '*'
                    q.append((nx, ny))
    return "KAKTUS"

for x in range(n):
    for y in range(m):
        if woods[x][y] == 'S': #고슴도치의 위치 넣어둔다
            q.append((x, y))
        elif woods[x][y] == 'D': #비버의 위치 넣어둔다
            Dx, Dy = x, y

for x in range(n): # 
    for y in range(m):
        if woods[x][y] == '*':
            q.append((x, y))

print(bfs(Dx, Dy))