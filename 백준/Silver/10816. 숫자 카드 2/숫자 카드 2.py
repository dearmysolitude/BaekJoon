import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 상근이가 가지고 있는숫자 카드의 개수
Cards = sorted(list(map(int, input().split()))) # 숫자 카드에 적혀있는 정수
M = int(input().rstrip()) # M, 주어진 정수
Nums = list(map(int, input().split())) # 상근이가 가지고 있는 카드 중 구해야 할 카드

count = {}
for card in Cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def bs(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target > arr[mid]:
        return bs(arr, target, mid+1, end)
    elif target < arr[mid]:
        return bs(arr, target, start, mid-1)
    else:
        return count.get(target)


for k in Nums:
    print(bs(Cards, k, 0, len(Cards)-1), end=' ')