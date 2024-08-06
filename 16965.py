from collections import deque
n = int(input())
l = []
for _ in range(n):
    o, a, b = map(int, input().split())
    if o == 1:
        l.append((a, b))
    else:
        a -= 1
        b -= 1
        r = set()
        for i in range(len(l)):
            for j in range(len(l)):
                x1, y1 = l[i]
                x2, y2 = l[j]
                if (x2 < x1 < y2) or (x2 < y1 < y2):
                    r.add((i, j))
        v = [False] * len(l)
        q = deque([a])
        v[a] = True
        f = False
        while q:
            c = q.popleft()
            if c == b:
                f = True
                break
            for n in r:
                if n[0] == c and not v[n[1]]:
                    q.append(n[1])
                    v[n[1]] = True
        if f:
            print(1)
        else:
            print(0)