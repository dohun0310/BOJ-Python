s = [0] * 5
for i in range(5):
    l = 0
    l = list(map(int, input().split()))
    s[i] = sum(l)
print(s.index(max(s)) + 1, max(s))