n = int(input())
p = input().split("*")
for i in range(n):
    t = input()
    if len(t) < len(p[0]) + len(p[1]):
        print("NE")
    else:
        if t[:len(p[0])] == p[0] and t[-len(p[1]):] == p[1]:
            print("DA")
        else:
            print("NE")