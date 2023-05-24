import sys
input = sys.stdin.readline

N = int(input().rstrip())
times = list(map(int, (input().split())))

# 모든 사람이 인출하는 시간의 합이 최소가 되려면 겹치는 시간(뒤에 대기하는 사람들)이
# 작은 시간들이 되어야 한다.
# 즉 제일 먼저 처리해야 하는 사람들은 시간이 가장 오래걸리는 사람들임

def atm(arr):
    ans = 0
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1):
            ans += arr[j]
    print(ans)

atm(times)