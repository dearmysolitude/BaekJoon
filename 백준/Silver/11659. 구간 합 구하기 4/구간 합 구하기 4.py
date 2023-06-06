
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(N+1):
    dp[i] = dp[i-1] + nums[i-1]
for _ in range(M):
    i, j  = map(int, input().split())
    ans = 0
    ans = dp[j] - dp[i-1]
    print(ans)