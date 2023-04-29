import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+1)
N = int(input().rstrip())
table = [0] * (N+2)
table[1] = 1
table[2] = 2

for i in range(3, N+1):
    table[i] = (table[i-1]+table[i-2])%15746
print(table[N])