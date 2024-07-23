n, b = map(int, input().split())
s = ""
a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while n:
    s += str(a[n % b])
    n //= b
print(s[::-1])