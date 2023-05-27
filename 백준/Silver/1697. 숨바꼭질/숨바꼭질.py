import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
# N = 수빈이가 있는 위치 K = 동생이 있는 위치
# 최소 조작 횟수를 찾으므로 bfs를 생각할 수 있다.

MAX = 100001
array = [0]*MAX # 여기까지 오는 횟수

def hideNseek(n):
    q = deque([n]) 
    while (q):
        n = q.popleft()
        if n == K:
            return array[n]
        for next_n in (n-1, n+1, 2*n): # 이렇게도 쓸 수 있군
            if 0 <= next_n < MAX and not array[next_n]: #큐에 있다면 최소 값에서 움직여야 한다
                array[next_n] = array[n] +1
                q.append(next_n)
print(hideNseek(N))
