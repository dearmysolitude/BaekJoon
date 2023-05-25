import sys
input = sys.stdin.readline

# N = int(input().rstrip())
# dp = [0] * (N+1) # dp[i] 는 i 를 연산으로 1로 만드는데 필요한 최소 연산의 수

# def oneMaker(n):
#     if (n == 1):
#         print(dp[1])
#         return
#     elif (n == 2):
#         dp[2] = 1
#         print(dp[2])
#         return
#     elif (n > 2):
#         dp[2] = 1
#         for i in range(3, n+1):
#             if (i % 3 == 0): # 3으로 나누어진다면, 1 뺀 애의 값이랑 비교
#                 a = int(i / 3)
#                 c = int(i - 1)
#                 dp[i] = min(dp[a], dp[c]) + 1
#             else:
#                 if (i % 2 == 0):
#                     b = int(i / 2)
#                     c = int(i - 1)
#                     dp[i] = min(dp[b], dp[c]) + 1
#                 else:
#                     c = int(i - 1)
#                     dp[i] = dp[int(i-1)] + 1
#     print(dp[n])
#     return

# oneMaker(N)

x=int(input()) # 수 입력받기
d=[0]*(x+1) # 1-based
for i in range(2,x+1): # 2부터 x까지 반복
    d[i]=d[i-1]+1 # 1을 빼는 연산 -> 1회 진행
    if i%2==0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i]=min(d[i],d[i//3]+1)
print(d[x])
