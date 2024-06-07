import statistics
n = int(input())
l = [0, 0, 0] * n
s = [0] * n
for i in range(n):
    l = list(map(int, input().split()))
    if len(set(l)) == 3:
        s[i] = max(l) * 100
    elif len(set(l)) == 2:
        s[i] = 1000 + statistics.mode(l) * 100
    else:
        s[i] = 10000 + l[0] * 1000
print(max(s))