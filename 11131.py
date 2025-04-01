for i in range(int(input())):
    n = input()        
    w = sum(map(int, input().split()))
    if w > 0:
        print("Right")
    elif w < 0:
        print("Left")
    else:
        print("Equilibrium")