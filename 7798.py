for i in range(1, int(input()) + 1):
    d, e = map(int, input().split())
    f = []
    for j in range(d):
        g, h, k, l, m = input().split()
        g, h, k, l = map(int, [g, h, k, l])
        n = ("A" if 20 <= g <= 35 else "B" if 36 <= g <= 48 else "C" if 49 <= g <= 62 else "")
        f.append((g, h, k, l, m, n))
    print(f"Case #{i}:")
    for j in range(e):
        o, p, q = input().split()
        p, q = int(p), int(q)
        r, s = -1, 0
        for t, (u, v, w, x, y, z) in enumerate(f):
            if o[0] != z or min(v, q) * w < p:
                continue
            a = (p + min(v, q) - 1) // min(v, q)
            if r == -1 or a * x < s or (a * x == s and u > f[r][0]):
                r, s = t, a * x
        if r != -1:
            print(f"{s} {f[r][4]}")
        else:
            print("no-hotel")