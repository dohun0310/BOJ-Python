l = list(input().upper())
s = []
for i in set(l):
    s.append(l.count(i))
if s.count(max(s)) > 1:
    print("?")
else:
    print(list(set(l))[s.index(max(s))])