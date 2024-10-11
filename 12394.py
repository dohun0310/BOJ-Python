for i in range(int(input())):
    a, b = map(int, input().split())
    l = list(map(float, input().split()))
    s = b + 2
    c = 1.0
    for j in range(1, a + 1):
        c *= l[j - 1]
        s = min(s, (a - j) + (c * (b - j + 1)) + ((1 - c) * (b - j + 1 + b + 1)))
    print(f"Case #{i + 1}: {s:.6f}")