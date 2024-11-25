import sys
s, e, q = sys.stdin.readline().rstrip().split()
s, e, q = int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:]), int(q[:2]) * 60 + int(q[3:])
l = set()
a = 0
while True:
    try:
        t, n = sys.stdin.readline().rstrip().split()
        t = int(t[:2]) * 60 + int(t[3:])
        if t <= s:
            l.add(n)
        elif n in l and e <= t <= q:
            l.remove(n)
            a += 1
    except:
        break
print(a)