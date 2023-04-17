import sys
N = int(input())
def stack(N):
    stack = []
    top = 0
    for i in range(N):
        user_input= sys.stdin.readline().split()
        if user_input[0] == 'push':
            stack.append(int(user_input[1]))
            top += 1
        elif user_input[0] == 'pop':
            if len(stack) != 0:
                print(stack.pop())
                top -= 1
            else: print(-1)
        elif user_input[0] == 'size':
            print(len(stack))
        elif user_input[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif user_input[0] == 'top':
            if len(stack) != 0:
                print(stack[top-1])
            else: print(-1)
stack(N)