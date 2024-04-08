r = int(input())
l = []
for i in range(r):
    l.append(input())
s = list(set(l))
s.sort()
s.sort(key = len)
for i in s:
    print(i)