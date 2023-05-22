import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def BinomCoe(n, k):
    ans = 1
    for i in range(k+1, n+1):
        ans *= i
    for j in range(1, n-k+1):
        ans /= j 
    print(int(ans))

BinomCoe(N, K)