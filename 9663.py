import sys
def check(x):
    for i in range(x):
        if l[x] == l[i] or abs(l[x] - l[i]) == abs(x - i):
            return False
    return True
def backtrack(x):
    global c
    if x == n:
        c += 1
        return
    for i in range(n):
        l[x] = i
        if check(x):
            backtrack(x + 1)
n = int(sys.stdin.readline())
l = [0] * n
c = 0
backtrack(0)
print(c)