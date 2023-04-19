import sys
a, b, c = map(int, sys.stdin.readline().split())

def DaC(a, b):
    global c
    if b == 1:
        return a % c
    
    temp = DaC(a, b//2)
    if b %2 == 0:
        return temp * temp % c
    if b % 2 != 0:
        return temp * temp * a % c
    
print(DaC(a, b))