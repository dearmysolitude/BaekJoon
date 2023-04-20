import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def sol(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1): # start는 판단 기준이 된다.
        if arr[start] < arr[i]:
            mid = i
            break
    sol(start+1, mid-1)
    sol(mid, end)
    print(arr[start])
sol(0, len(arr)-1)