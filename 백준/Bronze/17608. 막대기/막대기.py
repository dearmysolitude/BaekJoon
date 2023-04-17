import sys
N = int(input())
def canSee(arr):
    canbeSeen = []
    canbeSeen.append(arr[-1])
    j = 0
    for i in range(len(arr)-1, -1, -1): #역순, 역시 증가할 때와 동일하게 시작은 포함, 끝은 미포함
        if arr[i] > canbeSeen[j]:
            canbeSeen.append(arr[i])
            j += 1
    print(len(canbeSeen))

sticks = [int(sys.stdin.readline().strip()) for _ in range(N)]
canSee(sticks)