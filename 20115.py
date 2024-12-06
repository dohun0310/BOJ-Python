n = int(input())
l = list(map(int,input().split()))
m = max(l)
l.remove(m)
for i in l:
    m += i / 2
print(m)