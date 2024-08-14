import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().rstrip()
s = 0
t = ""
for i in a:
    if i.isdigit():
        t += i
    else:
        s += int(t)
        t = ""
s += int(t)
print(s - sum(range(1, n)))