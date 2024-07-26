n = int(input())
l = list(map(int, input().split()))
s = []
for i in range(1, n + 1):
    s.insert(l[i - 1], i)
print(*s[::-1])