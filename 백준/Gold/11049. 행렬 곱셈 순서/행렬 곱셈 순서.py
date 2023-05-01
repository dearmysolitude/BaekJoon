import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N+1)]

for i in range(2, N+1): # i는 글자 수
    for j in range(N-i+1):
        dp[i][j] = 2**32
        for k in range(1, i):
            dp[i][j] = min(dp[i][j], dp[i-k][j]+dp[k][j+i-k] + mat[j][0]*mat[j+i-k][0]*mat[j+i-1][1])
            # 계단형으로 올라가는 배열 구현
print(dp[-1][0])