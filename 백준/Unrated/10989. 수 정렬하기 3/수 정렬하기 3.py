import sys
tc = int(input())
nums = [0] * 10001

for i in range(tc):
    input = int(sys.stdin.readline())
    nums[input] += 1

for i in range(len(nums)):
    for k in range(nums[i]):
        if nums[i] != 0:
            print(i)
