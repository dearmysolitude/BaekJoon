import sys
input = sys.stdin.readline

NMax = 91
intro = int(input().rstrip())
table = [0] * (NMax+1)
table[1] = 1
table[2] = 1

def fibo(n):
    if 2 <= n <= NMax:
        if table[n] == 0:
            table[n] = fibo(n-1) + fibo(n-2)
        return table[n]
        # else:
        #     return fibo(n-1) +fibo(n-2)
    else:
        return 0
print(fibo(intro+1))