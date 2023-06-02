import sys
input = sys.stdin.readline

N, M = map(int, input().split())

notHeard = {}
listofnobody = [] * 500000
for i in range(N):
    notHeard[input().rstrip()] = 'notHeard'
for j in range(M):
    cnd = input().rstrip()
    # print(cnd)
    if(cnd in notHeard):
        listofnobody.append(cnd)
        # print('finding', listofnobody)
listofnobody.sort()
print(len(listofnobody))
for i in range(len(listofnobody)):
    print(listofnobody[i])