n, m = map(int, input().split())
a = set()
b = set()
s = []
for i in range(n):
    a.add(input())
for i in range(m):
    b.add(input())
for i in a:
    if i in b:
        s.append(i)
s.sort()
print(len(s))
for i in s:
    print(i)