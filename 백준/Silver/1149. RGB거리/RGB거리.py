import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 집의 수
RGB = [None] * N # index의 집을 red, green, blue 로 칠하는 비용의 list
dp = [[0 for _ in range (3)] for _ in range(N+1)] # index까지 칠해진 최소 비용, **각 색을 선택했을 경우에**

for i in range(N):
    RGB[i] = list(map(int, input().split()))

def min_cost(N, dp, arr):
    dp[0][0] = dp[0][1] = dp[0][2] = 0

    for i in range(1, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i-1][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i-1][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i-1][2]

    print(min(dp[N]))

min_cost(N, dp, RGB)