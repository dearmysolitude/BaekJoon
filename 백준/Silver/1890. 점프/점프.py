import sys
input = sys.stdin.readline

N = int(input().rstrip())
game = []
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1 ## 이 위치까지 올 수 있는 가짓수
for _ in range(N):
    game.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if game[i][j] != 0 and dp[i][j] !=0:
            if i + game[i][j]<N: # 갈 수 있는 곳에 현재 자리까지 올 수 잇는 방법 수를 더한다
                dp[i+game[i][j]][j] += dp[i][j]
            if j + game[i][j]<N:
                dp[i][j+game[i][j]] += dp[i][j]

print(dp[N-1][N-1])
