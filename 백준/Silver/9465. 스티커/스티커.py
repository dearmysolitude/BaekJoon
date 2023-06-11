import sys
input = sys.stdin.readline

def find(n, arr):
    for i in range(1, n):
        if i == 1:
            arr[0][1] += arr[1][0]
            arr[1][1] += arr[0][0]
        else:
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    return(max(arr[0][-1], arr[1][-1]))

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    print(find(N, sticker))