n = int(input())
l = list(map(int, input().split()))
t, p = map(int, input().split())
s = 0
for i in l:
    a = (i + t - 1) // t
    s += a
print(s)
print(n // p, n % p)