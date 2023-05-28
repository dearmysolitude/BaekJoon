import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic1 = {} # 키 값을 번호로
dic2 = {} # 키 값을 이름으로
for i in range(N):
    name = input().rstrip()
    dic1[i+1] = name # 여기 키 값만 int로 저장된다.
    dic2[name] = i+1
find = [None] * M
for j in range(M):
    find[j] = input().rstrip()

def findpoke(dic_1, dic_2, find_array):
    for k in range(len(find_array)):
        idx = find_array[k]
        if idx.isdecimal():
            print(dic_1.get(int(idx)))
        else:
            print(dic_2.get(idx))

findpoke(dic1, dic2, find)