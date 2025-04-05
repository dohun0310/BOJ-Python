import sys
n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
c = 0
for i in range(len(l) + 1)[::-1]:
    for j in range(i - 1):
        if l[j] > l[j + 1]:
            c += 1
            l[j], l[j + 1] = l[j + 1], l[j]
            if c == k:
                print(*l)
                exit()
print(-1)