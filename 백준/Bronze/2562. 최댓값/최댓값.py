def sol10(nums):
    maximum = 0
    i = 0
    for num in nums:
        if maximum < num:
            maximum = num
            maxindex = i
        i += 1
    print(maximum)
    print(maxindex+1)
# numbers = [int(input()) for _ in range(9)]
numbers=[]
for i in range(9):
    numbers.append(int(input()))
sol10(numbers)