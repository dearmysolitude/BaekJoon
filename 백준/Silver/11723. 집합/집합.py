import sys

input = sys.stdin.readline
N = int(input().rstrip())

# 어떤 자료구조 써야하나? 링크드 리스트?
# 카운트 소트?
# 리스트의 인덱스를 특정 값으로 두고 그 인덱스의 값을 있는지1 없는지0 판단하는 데 써보자
# 출제 의도 -> 비트마스킹

NUMBERS = 21
nums = [0] * NUMBERS
EXIST = 1
EMPTY = 0

def operate(n, array):
    operation = [None] * 2
    for _ in range(n):
        operation = list(map(str, input().split())) #이렇게 받으면 뒤에 없는 경우 operation 요소가 하나로 줄음
        order = operation[0]
        if order != 'all' and order != 'empty': 
            x = int(operation[1])
        if order == 'add':
            array[x] = EXIST
        elif order == 'remove':
            array[x] = EMPTY
        elif order == 'check':
            if array[x] == EXIST:
                print(EXIST)
            else:
                print(EMPTY)
        elif order == 'toggle':
            if array[x] == EXIST:
                array[x] = EMPTY
            else:
                array[x] = EXIST
        elif order == 'all':
            for i in range(1, NUMBERS):
                array[i] = EXIST
        else:
            for i in range(1, NUMBERS):
                array[i] = EMPTY
            
operate(N, nums)