def sol20(square, num, cuts) -> None:
    pla = 0
    hor = 0 #자르는 횟수#
    plaPoints = []
    horPoints = []
    if num != 0: #예외 처리
        for i in range(0, num):
            if (cuts[i][0] == 0): #가로로 자른다면
                pla += 1 #가로로 자르는 횟수
                plaPoints.append(cuts[i][1])
            else: #세로로 자른다면
                hor += 1 #세로로 자르는 횟수
                horPoints.append(cuts[i][1])
    elif num == 0:
        print(square[0]*square[1])
        return
    # 리스트 오름차순으로 정렬 각 좌표계의 0과 최대값을 추가하여 나중에 길이를 만들 for문이 복잡해지지 않도록 하자
    # pla와 hor하나씩 추가하여 #길이 수#로 맞춰준다.
    plaPoints.sort()
    horPoints.sort()
    plaPoints.insert(0, 0)
    plaPoints.append(square[1]) #주의: 가로로 자른 경우 좌표의 최대값은 y축임
    pla += 1
    horPoints.insert(0, 0)
    horPoints.append(square[0]) #
    hor += 1
    #길이들의 리스트를 만들어 값들을 추가하여보자. 가로로 잘라서 만들어진 길이는 y축 상에 있으므로 세로라고 표기해야 맞지만 편의상 plaLen으로 한다
    plaLen = []
    horLen = []
    for j in range(0, pla):
        plaLen.append(plaPoints[j+1]-plaPoints[j])
    for k in range(0, hor):
        horLen.append(horPoints[k+1]-horPoints[k])
    # 다시 오름차순 정럴하여 가장 큰 면적을 구하면 된다.
    plaLen.sort()
    horLen.sort()
    Biggist = plaLen[-1]*horLen[-1]
    print(Biggist)
    return

# sq = [10, 8]
# numb = 3
# cuts = [[0, 3], [1, 4], [0, 2]]

sq = list(map(int, input().split())) # list(int(input().split()))
numb = int(input())
cuts = [list(map(int, input().split())) for _ in range(numb)]
sol20(sq, numb, cuts)