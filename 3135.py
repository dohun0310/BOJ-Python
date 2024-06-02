a, b = map(int, input().split())
n = int(input())
j = abs(a - b)
for i in range(n):
    f = int(input())
    if f == b:
        j = 1
        break
    else:
        if j > abs(f - b):
            j = abs(f - b) + 1
print(j)