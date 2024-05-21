t = int(input())
l = [[""]] * t
a = 0
for i in range(t):
    l[i] = input().split(" ")
for i in l:
    for j in i:
        print("".join(reversed(j)), end=" ")
    print()