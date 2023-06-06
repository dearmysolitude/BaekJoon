import sys
from collections import deque
input = sys.stdin.readline

# 목표 지점부터 시작한다.
def navi(arr, y, x, n, m): # 목표지점의 좌표를 넣어..
    q = deque()
    q.append([y, x])
    arr[y][x] = 0
    desX = x
    desY = y
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        y, x = map(int, q.popleft())
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < m and 0 <= ny < n and arr[ny][nx] == 1):
                if arr[ny][nx] == 0:
                    continue
                q.append([ny, nx])
                arr[ny][nx] += arr[y][x]

    for i in range(n): # 못가는 데는 -1로
        for j in range(m):
            if (arr[i][j] == 1):
                arr[i][j] = -1

    for i in range(4): # 2근처를 1로 만들기 위함
        x = desX + dx[i]
        y = desY + dy[i]
        if 0 <= x < m and 0 <= y < n and arr[y][x] == 3: # 중복할 경우 최종 목적지 근처 값은 3이 된다.
            arr[y][x] = 1

n, m = map(int, input().split())  # n은 세로의 크기, m은 가로의 크기
coor = [None] * n
for i in range(n):
    coor[i] = list(map(int, input().split()))

# 목표점을 찾는다
for i in range(n):
    for j in range(m):
        if coor[i][j] == 2:
            destX = j
            destY = i
            
navi(coor, destY, destX, n, m)

for i in range(n):
    for j in range(m):
        print(coor[i][j], end=' ')
    print()