import sys
def bt(t, x):
    c = 0
    if x == len(s):
        return 1
    for k in d:
        if k == t or d[k] == 0:
            continue
        d[k] -= 1
        c += bt(k, x + 1)
        d[k] += 1
    return c
s = list(sys.stdin.readline().strip())
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(bt("", 0))