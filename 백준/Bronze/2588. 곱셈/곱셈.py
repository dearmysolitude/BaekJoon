inputs = [input() for _ in range(2)]

def sol2(A, B):
    BH = B//100
    BD = B//10 - 10* BH
    BA = B - BH * 100 -BD * 10
    print(A * BA, A * BD, A * BH, A * B, sep='\n')
    return

a = int(inputs[0])
b = int(inputs[1])

sol2(a, b)