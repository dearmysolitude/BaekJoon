import sys
def sol14(chars, num):
    for i in range(0, num):
        mul = int(chars[i][0]) # multiplication
        char = list(chars[i][1]) #문자열
        for k in range(0, len(char)):
            print(char[k]*mul, end='')
        print('')
numb = int(input())
chars = [sys.stdin.readline().split() for _ in range(numb)]
sol14(chars, numb)