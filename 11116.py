from collections import deque
n = int(input())
for i in range(n):
    m = int(input())
    l, r = deque(map(int, input().split())), deque(map(int, input().split()))
    c, s = 0, 0
    while l:
        t = l.popleft()
        if t + 1000 in r:
            c += 1
        if c == 2:
            c = 0
            s += 1
    print(s)