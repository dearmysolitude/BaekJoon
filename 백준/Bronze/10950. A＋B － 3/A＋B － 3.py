i = int(input())
arr = [[0]*2 for _ in range(i)]
for k in range(i):
    arr[k] = list(map(int, input().split()))

#nums = [list(map(int, input().split)) for _ in range(i)]
def sol7(list, k):
    for i in range(k):
        print(list[i][0] + list[i][1])
sol7(arr, i)