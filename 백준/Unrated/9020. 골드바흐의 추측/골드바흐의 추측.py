import sys, math
def prime(number):
    if number == 1:
        return False
    else:
        i = 2
        while i <= math.ceil(number/2): #2 , 짝수!
            if(number % i == 0):
                return False
            i += 1
        return True
def goldbach(numbers):
    for number in numbers:
        base = int(number/2)
        for i in range(0, base):
            a = base + i
            b = base - i
            if (prime(a) == True and prime(b) == True):
                print(b, a)
                break

n = int(input())
nums = list(int(sys.stdin.readline()) for _ in range(n))
goldbach(nums)