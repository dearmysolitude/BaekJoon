a = int(input())
nums = []

def sol(nums, a):
    flag = 0
    nums.append(a)
    while True:
        num = nums[flag]
        if flag != 0 and num == a:
            print(flag)
            return    
        if num < 10:
            num = num*10 + num
            nums.append(num)
            flag += 1
            continue
        # 십
        second = num // 10 # 십의 자리
        # 일
        first =  num - second*10 #일의 자리

        n1 = first + second

        n2 = n1 % 10 #합의 일의자리
        
        num = n2 + first*10

        nums.append(num)
        flag += 1

sol(nums, a)