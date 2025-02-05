from collections import deque
for i in range(1, int(input()) + 1):
    n = int(input())
    l = deque(map(int, input().split()))
    while True:
        if len(l) == 2:
            break
        t = deque()
        while l:
            t.append(l[0] + l[-1])
            l.popleft()
            if l:
                l.pop()
        l = t
    if l[0] > l[1]:
        print(f"Case #{i}: Alice")
    else:
        print(f"Case #{i}: Bob")