a, b = map(int, input().split())
houses = list(int(input()) for _ in range(a))
ans = 0

def sol3(house, N, arr): #house: 집의 수, N: 공유기 수, arr: 집의
    global ans
    arr.sort()
    right = arr[-1] - arr[0] # 길이의 최대값
    left = 1 # 길이의 최소값: 허용 가능함
    while left <= right:
        mid = (left + right) // 2 # 근접값을 이 값으로 설정했을 때 모두 배치할 수 있는가?(조건 만족시킬 수 있는가?)
        # 최대한 멀리 설치해야 한다 -> 첫번째 집에는 무조건 설치해야 한다.
        installed = arr[0]
        count = 1
        for i in range(1, house):
            if arr[i] - installed >= mid:
                installed = arr[i]
                count += 1
                if count == N: break
        if count == N: #**
            left = mid + 1
            ans = mid
        elif count < N:
            right = mid - 1
sol3(a, b, houses)
print(ans)