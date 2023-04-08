import math
def sol17(a, b, v):
    n = (v-a)/(a-b)+1
    ans = math.ceil(n)
    print(ans)
num1, num2, num3 = map(int, input().split())
sol17(num1, num2, num3)