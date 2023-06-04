import sys
import heapq
input = sys.stdin.readline

def worker(num):
    ascend = []
    descend = []
    deleted = [True]*num
    for i in range(num):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(ascend, (-n, i))
            heapq.heappush(descend, (n, i))
            deleted[i] = False
        else:
            if n == 1:
                while ascend and deleted[ascend[0][1]]: # 이미 삭제됐다면 팝해버림
                    heapq.heappop(ascend)
                if ascend:
                    deleted[ascend[0][1]] = True
                    heapq.heappop(ascend)
            else:
                while descend and deleted[descend[0][1]]:
                    heapq.heappop(descend)
                if descend:
                    deleted[descend[0][1]] = True
                    heapq.heappop(descend)

    while ascend and deleted[ascend[0][1]]:
        heapq.heappop(ascend)
    while descend and deleted[descend[0][1]]:
        heapq.heappop(descend)

    if ascend and descend:
        print(-ascend[0][0], descend[0][0])
    else:
        print('EMPTY')

T = int(input().rstrip()) # test case 수
for _ in range(T):
    num = int(input().rstrip()) #command 수
    worker(num)