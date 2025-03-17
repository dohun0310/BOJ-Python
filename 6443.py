import sys
def back(c):
    if c == len(l):
        print(*s, sep="")
        return
    for k in v:
        if v[k]:
            v[k] -= 1
            s.append(k)
            back(c + 1)
            v[k] += 1
            s.pop()

for i in range(int(sys.stdin.readline())):
    l = sorted(list(map(str, sys.stdin.readline().strip())))
    v = {}
    s = []
    for j in l:
        if j not in v:
            v[j] = 1
        else:
            v[j] += 1
    back(0)