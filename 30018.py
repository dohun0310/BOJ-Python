n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
for i in range(n):
    s += abs(a[i] - b[i])
print(s // 2)