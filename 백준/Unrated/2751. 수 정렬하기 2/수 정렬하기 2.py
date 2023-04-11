import sys
def sort(nums):
    nums.sort()
    for i in range(len(nums)): print(nums[i])
    return
tc = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(tc)]
sort(numbers)