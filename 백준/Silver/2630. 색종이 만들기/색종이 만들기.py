import sys
N = int(input())
cube = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(cube)

b_cnt = 0
w_cnt = 0
def sectionCount(arr, startX, startY, N): # 한 구역이 채워져 있는지 아닌지 확인하는 함수
    tmp_cnt = 0
    global b_cnt
    global w_cnt
    for i in range(startX, startX+N):
        for j in range(startY, startY+N):
            if arr[i][j]:                    # 이렇게도 쓸 수 있다.
                tmp_cnt += 1
    if not tmp_cnt: # 아무것도 없음! 값들이 모두 0
        w_cnt += 1
    elif tmp_cnt == N**2:
        b_cnt += 1
    else: # 나누어지는 다음 단계를 모두 재귀한다
        sectionCount(arr, startX, startY, N//2)  #나머지 없이 몫으로 나누면 1칸까지 커버 가능
        sectionCount(arr, startX + N//2, startY, N//2)
        sectionCount(arr, startX, startY + N//2, N//2)
        sectionCount(arr, startX + N//2, startY + N//2, N//2)
    return
sectionCount(cube, 0, 0, N)
print(w_cnt)
print(b_cnt)