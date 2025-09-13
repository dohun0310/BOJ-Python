n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum(a)
for i in b:
    if i == 0:
        continue
    s *= i
print(s)