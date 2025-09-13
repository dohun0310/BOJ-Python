n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
p = 0
for i in range(n)[::-1]:
    p += a[i] - 1
    if m <= p:
        break
if m > p:
    print("OUT")
else:
    print("DIMI")