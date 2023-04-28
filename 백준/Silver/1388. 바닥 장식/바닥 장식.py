
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #방 바닥의 세로 크기 / 방 바악의 가로 크기

floor = []
for i in range(N):
    floor.append(list(map(str, input().rstrip())))
# for j in range(N):
#     print(floor[j])

count = 0
def dfsP(x, y):
    ny = y + 1
    floor[y][x] = '1'
    if ny < N and floor[ny][x] == '|' :
        dfsP(x, ny)

def dfsH(x, y):
    nx = x + 1
    floor[y][x] = '1'
    if nx < M and floor[y][nx] == '-':
        dfsH(nx, y)

def sol():
    global count
    for i in range(M):
        for j in range(N):
            if floor[j][i] == '-':
                dfsH(i, j)
                count += 1
            elif floor[j][i] == '|':
                dfsP(i, j)
                count += 1
    print(count)

sol()
