def sol5(compareList):
    list = [compareList[2] - compareList[0], compareList[0], compareList[3] - compareList[1], compareList[1]]
    # a = min(list)  iterable 자료형인 경우 iteration에 있는 첫 번째 요소를 리턴
    a = min(list)
    return print(a)
compareList = list(map(int, input().split()))
sol5(compareList)