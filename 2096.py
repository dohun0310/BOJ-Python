n = int(input())
l = list(map(int, input().split()))
a, b = l, l
for i in range(n - 1):
    l = list(map(int, input().split()))
    a = [l[0] + max(a[0], a[1]), l[1] + max(a), l[2] + max(a[1], a[2])]
    b = [l[0] + min(b[0], b[1]), l[1] + min(b), l[2] + min(b[1], b[2])]
print(max(a), min(b))