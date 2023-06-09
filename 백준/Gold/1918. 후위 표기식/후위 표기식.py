import sys
input = sys.stdin.readline

infix = list(input().rstrip())

def itop(arr):
    operator = []
    postfix = []

    for i in arr:
        if  i == '(':
            # print(1)
            operator.append(i)
        elif i == '+' or i == '-':
            # print(2)
            while operator and operator[-1] != '(':
                postfix += operator.pop()
            operator.append(i)
        elif i == '*' or i == '/':
            # print(3)
            while operator and (operator[-1] == '/' or operator[-1] == '*'):
                postfix += operator.pop()
            operator.append(i)
        elif i == ')':
            # print(4)
            while operator and operator[-1] != '(':
                postfix += operator.pop()
            operator.pop()
        else:
            # print(5)
            postfix.append(i)
        # print(operator)
        # print('ans =', postfix)
    while operator:
        postfix += operator.pop()
        
    for j in postfix:
        print(j, end='')

itop(infix)