n = int(input())
t = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    t[i] = a - b
t.sort()
if n % 2:
    print(1)
else:
    print(abs(t[n // 2] - t[n // 2 - 1]) + 1)