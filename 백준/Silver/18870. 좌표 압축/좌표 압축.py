import sys
input = sys.stdin.readline

N = int(input().rstrip())
origin_nums = [] * N
origin_nums = list(map(int, input().split()))
nums = list(sorted(set(origin_nums))) # 이 배열의 인덱스가 압축된 좌표임

def binary(arr, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if target < arr[mid]:
        return binary(arr, target, start, mid)
    elif target > arr[mid]:
        return binary(arr, target, mid+1, end)
    elif target == arr[mid]:
        return mid

for j in origin_nums:
    ans = binary(nums, j, 0, len(nums))
    print(ans, end=' ')