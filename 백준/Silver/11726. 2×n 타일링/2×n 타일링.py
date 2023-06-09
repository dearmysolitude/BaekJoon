import sys
input = sys.stdin.readline

N = int(input().rstrip())

def TwobyN(n):
    dp = [0 for i in range(n+2)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+2):
        dp[i] = (dp[i-2] + dp[i-1]) % 10007
    print(dp[n])
    return

TwobyN(N)