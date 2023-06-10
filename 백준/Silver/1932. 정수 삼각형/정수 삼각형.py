import sys
input = sys.stdin.readline

# dp ?

N = int(input().rstrip())
dp = [[0 for _ in range(i+1)] for i in range(N)]
# 기존 삼각형과 동일한 형태의 dp테이블.
# 삼각형에서 겹치는 원소-마지막이 같은 경로를 거친 것-는 큰 것을 받으면 
# 테이블이 더 깔끔해지고 원소 접근도 쉬워진다. - 원래는 모든 합 경로를 다 쓰려고 했었음
triangle = [list(map(int, input().split())) for _ in range(N)]
dp[0][0] = triangle[0][0]

def biggest(N, arr, dp):
    for i in range(1, len(arr)):
        for j in range(len(arr[i-1])): 
            dp[i][j + 1] = max(dp[i][j+1], dp[i-1][j] + arr[i][j+1])
            dp[i][j] = max(dp[i][j], dp[i-1][j] + arr[i][j])
    return max(dp[-1])

print(biggest(N, triangle, dp))