import sys
l = [1] * 1000001
s = [0] * 1000001
s[1] = 1
for i in range(2, 1000001):
    for j in range(1, 1000000 // i + 1):
        l[i * j] += i
    s[i] = s[i - 1] + l[i]
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(s[n])