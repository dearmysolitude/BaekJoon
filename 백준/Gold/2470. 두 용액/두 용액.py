import sys
N = int(input())
solution = list(map(int, sys.stdin.readline().split()))
def sol4(arr):
    left = 0
    right = len(arr)-1
    arr.sort()
    smallest = [0, 0]
    now = 10000000000000000
    if arr[-1] < 0:
        smallest=[arr[-2], arr[-1]]
        print(smallest[0], smallest[1])
        return
    elif arr[0] > 0:
        smallest=[arr[0], arr[1]]
        print(smallest[0], smallest[1])
        return

    while left < right:
        toZero = abs(arr[left]+arr[right])
        if toZero < now:
             now = toZero
             smallest = [arr[left], arr[right]]
        if now == 0:
            break
        if arr[left] + arr[right] > 0:
            right = right - 1
        elif arr[left] + arr[right] < 0:
            left = left + 1

    print(smallest[0], smallest[1])
sol4(solution)