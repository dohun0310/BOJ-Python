n, k = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for i in l:
    c += (i + 1) // 2
if c >= n:
    print("YES")
else:
    print("NO")