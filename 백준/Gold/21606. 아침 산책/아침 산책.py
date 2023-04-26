import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 정점 수
A = list(map(int,list(input().strip()))) # 실내/외 여부 

graph = [[] for _ in range(n+1)] # 연결리스트
place = [0 for _ in range(n+1)] # 실내: 1, 실외: 0
visited = [False for _ in range(n+1)] # 방문 여부

# place  초기화
for i in range(len(A)):
    if A[i] == 1:
        place[i+1] = 1

# 연결리스트 입력
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs함수
def dfs(i):
    res = 0
    for next_node in graph[i]: ##이렇게 쓸 수도 있군
        if place[next_node] == 0: #다음 노드가 실외고
            if not visited[next_node]: #방문 안했으면
                visited[next_node] = True
                res += dfs(next_node)
        else: #실내라면
            res += 1
    return res

ans = 0
for i in range(1, n+1):
    if place[i] == 0: # 실외인 경우
        if not visited[i]:
            visited[i] = True
            res = dfs(i)
            ans += res * (res - 1)
    else: #실내인 경우 따로 더하면 된다
        for next_node in graph[i]:
            if place[next_node] == 1: # 연속된 실내인 경우
                ans += 1
print(ans)