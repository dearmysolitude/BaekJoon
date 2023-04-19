from collections import deque
N, K = map(int, input().split())
def josephus(n, k):
    q = deque(maxlen = n+1)
    ans = []
    for i in range(n):
        q.append(i+1)
    while len(q) != 0:
        q.rotate(-k+1)
        ans.append(q.popleft())
    print('<', end='')
    for i in range(n-1) :print(ans[i], end=', ')
    print(ans[-1], '>', sep='')
josephus(N, K)