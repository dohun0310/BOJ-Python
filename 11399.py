n = input()
l = list(map(int, input().split()))
l.sort()
s = 0
for i in range(len(l)):
    s += sum(l[:i + 1])
print(s)