while True:
    l = list(map(int, input().split()))
    if sum(l) == 0:
        break
    if max(l) < sum(l) - max(l):
        if len(set(l)) == 1:
            print("Equilateral")
        elif len(set(l)) == 2:
            print("Isosceles")
        elif len(set(l)) == 3:
            print("Scalene")
    else:
        print("Invalid")