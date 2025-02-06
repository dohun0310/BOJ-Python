a, b, c = map(int, input().split())
s = 1e9
for i in ("+", "-", "*", "//"):
    if i == "//" and a % b:
        continue
    t = eval(f"{a}{i}{b}")
    for j in ("+", "-", "*", "//"):
        if j == "//" and t % c:
            continue
        r = eval(f"{t}{j}{c}")
        if not r < 0:
            s = min(s, r)
print(s)