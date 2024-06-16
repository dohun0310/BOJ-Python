n, m = map(int, input().split())
s = set()
for i in range(n):
    s.add(input())
c = 0
for i in range(m):
    if input() in s:
        c += 1
print(c)