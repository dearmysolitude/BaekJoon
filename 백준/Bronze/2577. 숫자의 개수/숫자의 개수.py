def sol12(input):
    a = input[0]*input[1]*input[2]
    b = str(a)
    zero = b.count('0')
    one = b.count('1')
    two = b.count('2')
    three = b.count('3')
    four = b.count('4')
    five = b.count('5')
    six = b.count('6')
    seven = b.count('7')
    eight = b.count('8')
    nine = b.count('9')
    print(zero, one, two, three, four, five, six, seven, eight, nine, sep='\n')
nums = [int(input()) for _ in range(3)]
sol12(nums)