n, k = map(int, input().split())
l = list(input())
s = 0
for i in range(n):
    if l[i] == "P":
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if l[j] == "H":
                l[j] = 0
                s += 1
                break
print(s)