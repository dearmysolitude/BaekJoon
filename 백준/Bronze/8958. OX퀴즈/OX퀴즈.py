def sol11(inputs):
    for input in inputs:
        point = 0
        os = input.split('X')
        for k in os:
            a = len(k)
            for x in range(1, a+1):
                point += x
        print(point)

num = int(input())
ans = [input() for _ in range(num)]

sol11(ans)
