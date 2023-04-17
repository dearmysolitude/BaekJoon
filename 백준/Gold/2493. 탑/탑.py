import sys
N = int(input())
towers = list(map(int, sys.stdin.readline().split())) # 너는 이제부터 스택이다
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:
            answer.append(stack[-1][0]+1)
            break
        stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, towers[i]])
for i in range(N):
    print(answer[i], end=' ')