n = int(input())
s = 1000000000
for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        s = min(s, b)
print(s if s != 1000000000 else -1)