import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 최대공약수
# 유클리드 호제법 = 어떤 두 양수에 대하여 최대공약수는 한 수와 
# 나머지 한 수를 나눈 나머지의 최대공약수와 같다
def Euclidean(first, second):
    while second != 0:
        [first, second] = [second, first%second]
    return first

# 최소공배수
def lcm(first, second):
    for i in range(1, second+1):
        for j in range(1, first+1):
            if (first * i == second * j):
                return (first*i)

print(Euclidean(a, b))
print(lcm(a, b))