import sys
input = sys.stdin.readline

# test case ~100
t = int(input().rstrip())

# 같은 종류의 의상을 한가지 선택하는 방법(안 선택하는 방법까지 포함)
# 들을 종류별로 구하여 곱하면 된다. 여기서 마지막에 벌거벗는 1 만 빼자

def cClothes(N):
    cmd = [] * 2
    Sort= {} #clothes종류
    count = 1
    for i in range(N):
        cmd = list(map(str, input().split()))
        if Sort.get(cmd[1]) == None:
            Sort[cmd[1]] = 2
        else:
            Sort[cmd[1]] += 1
    for j in Sort.values():
        count *= j
    print(count-1)

# number of clothes
for _ in range(t):
    n = int(input().rstrip())
    cClothes(n)
