n = input()
l = list(map(int, input().split()))
m = max(l)
for i in l:
    l[l.index(i)] = i / m * 100
print(sum(l) / len(l))