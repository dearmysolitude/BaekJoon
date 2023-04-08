input = int(input())

def sol3(a):
    if a >= 90:
        print("A")
        return 
    elif a >= 80 and a < 90:
        print("B")
        return
    elif a >= 70 and a < 80:
        print("C")
        return
    elif a >= 60 and a < 70:
        print("D")
        return
    else:
        print("F")
        return
    
sol3(input)