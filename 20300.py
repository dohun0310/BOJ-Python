n = int(input())
t = list(map(int, input().split()))
t.sort()
s = 0
if len(t) % 2:
    s = t.pop(-1)
m = [0] * (len(t) // 2)
for i in range(len(t) // 2):
    m[i] = t[i] + t[-i - 1]
m.append(s)
print(max(m))