i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        exit()
    a = v // p
    b = v % p
    print(f"Case {i}: {a * l + min(l, b)}")
    i += 1