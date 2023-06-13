import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(1, N+1):
    arr.append(i)

nCr = itertools.combinations(arr, M)
a = list(nCr)

for i in range(len(a)):
    b = list(a[i])
    b.sort()
    for j in range(len(b)):
        print(b[j], end = ' ')
    print()