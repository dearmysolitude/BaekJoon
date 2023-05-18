import sys
from collections import deque
input = sys.stdin.readline

testcase = int(input())
q = deque()
def deque_test (x):
    if(x[0] == 'push_front'): #left를 end로, right를 front로.
        q.append(int(x[1]))
    elif(x[0] == 'push_back'):
        q.appendleft(int(x[1]))
    elif(x[0] == 'pop_front'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q.pop())
    elif(x[0] == 'pop_back'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q.popleft())
    elif(x[0] == 'size'):
        print(len(q))
    elif(x[0] == 'empty'):
        if(len(q) == 0):
            print(1)
        else:
            print(0)
    elif(x[0] == 'front'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q[-1])
    elif(x[0] == 'back'):
        if (len(q) == 0):
            print(-1)
        else:
            print(q[0])
    return

for _ in range(testcase):
    order = list(map(str, input().rstrip().split()))
    deque_test(order)