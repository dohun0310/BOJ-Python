n, m = input().split()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
s = a - b
print(len(s))
if len(a - b) > 0:
    print(*sorted(s))