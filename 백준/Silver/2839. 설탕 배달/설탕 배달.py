import sys
input = sys.stdin.readline

N = int(input().rstrip())

def findNum(weight):
    idx = weight // 5
    rest = 0
    for i in range(idx, -1, -1):
        rest = weight - (i*5)
        if rest % 3 == 0:
            return (i + int(rest//3))
        if i == 0 and rest // 3 == 0:
            return int(rest//3)
    return -1

print(findNum(N))