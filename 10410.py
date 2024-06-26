for i in range(int(input())):
    l = list(input().split())
    n, c = l[0], int(l[3])
    s = int(l[1].split("/")[0])
    b = int(l[2].split("/")[0])
    if s < 2010 and b < 1991 and c >= 41:
        print(n, "ineligible")
    elif s < 2010 and b < 1991 and c < 41:
        print(n, "coach petitions")
    else:
        print(n, "eligible")