import sys
n = list(sys.stdin.readline().rstrip())
l = []
for i in range(int(sys.stdin.readline())):
    c = sys.stdin.readline().split()
    if c[0] == "L" and n:
        l.append(n.pop())
    elif c[0] == "D" and l:
        n.append(l.pop())
    elif c[0] == "B" and n:
        n.pop()
    elif c[0] == "P":
        n.append(c[1])
print("".join(n + list(reversed(l))))