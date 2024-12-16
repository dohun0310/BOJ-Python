n = int(input())
a, b = map(int, input().split())
s = a // 2  + b
if n >= s:
    print(s)
else:
    print(n)