n = int(input())
l = list(map(int, input().split()))
s = [0] * n
for i in range(n):
    for j in range(n):
        if l[i] == 0 and s[j] == 0:
            s[j] += i + 1
            break
        elif s[j] == 0:
            l[i] -= 1
print(*s)