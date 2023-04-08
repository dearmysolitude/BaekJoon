def sol9(nums, input):
    for num in nums:
        if input > num:
            print(num, end=' ')

a, b = map(int, input().split())
nums = list(map(int, (input().split())))

sol9(nums, b)