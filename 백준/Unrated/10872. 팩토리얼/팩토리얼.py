def sol21(num,ans) -> None:
    if num > 1:
        ans = ans*num
        sol21(num-1, ans)
    elif num == 1 or num == 0:
        print(ans)
number = int(input())
sol21(number, 1)