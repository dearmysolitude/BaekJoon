def sol19(number):
    if number < 100:
        print(number)
    else:
        n = 99
        for num in range(100, number+1):
            nh = num // 100
            nt = num // 10 - nh*10
            no = num % 10
            if (nt*2 == (nh + no)):
                n += 1
        print(n)
num = int(input())
sol19(num)
