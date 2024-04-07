r = int(input())
for i in range(r):
    a, b = list(map(str, input().split()))
    for i in range(len(b)):
        print(b[i] * int(a), end="")
    print()