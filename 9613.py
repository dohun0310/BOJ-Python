import sys, math
t = int(sys.stdin.readline())
for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    s = 0
    for j in range(1, len(n)):
        for k in range(j + 1, len(n)):
            s += math.gcd(n[j], n[k])
    print(s)