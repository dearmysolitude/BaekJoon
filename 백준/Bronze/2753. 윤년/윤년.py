i = int(input())

def sol4(a):
    if (a % 400 == 0):
        return print(1)
    elif(a % 4 == 0 and a % 100 != 0):
        return print(1)
    else:
        return print(0)

sol4(i)