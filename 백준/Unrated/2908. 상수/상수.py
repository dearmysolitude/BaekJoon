def sol16(num1, num2):
    num1s = list(num1)
    num2s = list(num2)
    num1r = reversed(num1s) #반복자 타입으로 반환-메모리 상의 이득
    num2r = reversed(num2s) #반복자 타입으로 반환
    a = '' # string
    b = ''
    for letter in num1r:
        a += letter
    for letter2 in num2r:
        b += letter2
    if int(a) < int(b): #여기에서 형변환을 하여 비교했지만 실제 자료 값은 변하지 않음
        print(b)
    elif int(a) > int(b):
        print(a)
a, b = map(str, input().split())
sol16(a, b)