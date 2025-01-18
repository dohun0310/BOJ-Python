n, m = map(int, input().split())
l = [i for i in range(1, n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    l = l[:a - 1] + l[a - 1:b][::-1] + l[b:]
print(*l)