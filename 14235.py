l = []
for i in range(int(input())):
    n = list(map(int, input().split()))
    if n == [0]:
        if len(l) == 0:
            print(-1)
        else:
            print(l.pop())
    else:
        l.extend(n[1:])
        l.sort()