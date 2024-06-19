n = int(input())
l = [0, 1]
for i in range(2, abs(n) + 1):
    l.append((l[i - 1] + l[i - 2]) % 1000000000)
if n < 0 and n % 2 == 0:
    r = -l[abs(n)]
else:
    r = l[abs(n)]
if r == 0:
    print(0)
elif r > 0:
    print(1)
else:
    print(-1)
print(abs(r))