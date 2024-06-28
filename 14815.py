t = int(input().strip())
for i in range(1, t + 1):
    n, p = map(int, input().strip().split())
    l = list(map(int, input().strip().split()))
    c = [0] * p
    for j in l:
        c[j % p] += 1
    r = c[0]
    if p == 2:
        r += (c[1] + 1) // 2
    elif p == 3:
        m = min(c[1], c[2])
        r += m
        c[1] -= m
        c[2] -= m
        r += c[1] // 3
        r += c[2] // 3
        if c[1] % 3 > 0 or c[2] % 3 > 0:
            r += 1
    print(f"Case #{i}: {r}")