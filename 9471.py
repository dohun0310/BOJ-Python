p = int(input())
for i in range(p):
    n, m = map(int, input().split())
    f = [0, 1]
    while True:
        f.append((f[-1] + f[-2]) % m)
        if f[-1] == 1 and f[-2] == 0:
            break
    print(n, len(f) - 2)