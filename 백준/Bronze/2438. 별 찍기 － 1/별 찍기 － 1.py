num = int(input())
def sol8(a):
    for i in range(1, a+1):
        for j in range(1, i+1):
            print("*", end='')
        print('')
sol8(num)