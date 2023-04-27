import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    applied = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    applied.sort()
    min_rank = applied[0][1]
    cnt = 1
    for i in range(n):
        rank = applied[i][1]
        if rank < min_rank:
            min_rank = rank
            cnt += 1
    print(cnt)