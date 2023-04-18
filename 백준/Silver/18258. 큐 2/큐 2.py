import sys
from collections import deque
N = int(input())
def queue(N):
    q = deque()
    for i in range(N):
        user_input= sys.stdin.readline().split()
        if user_input[0] == 'push':
            q.append(user_input[1])

        elif user_input[0] == 'pop':
            if len(q) != 0:
                print(q.popleft())
            else: print(-1)

        elif user_input[0] == 'size':
            print(len(q))

        elif user_input[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)

        elif user_input[0] == 'front':
            if len(q) != 0:
                print(q[0])
            else: print(-1)

        elif user_input[0] == 'back':
            if len(q) != 0:
                print(q[-1])
            else: print(-1)
queue(N)