n = int(input())
s = list(map(int, input().split()))
for i in range(n - 1, 0, -1):
    if s[i - 1] > s[i]:
        for j in range(n - 1, 0, -1):
            if s[i - 1] > s[j]:
                s[i - 1], s[j] = s[j], s[i - 1]
                b = sorted(s[i:], reverse=True)
                s = s[:i] + b
                print(*s)
                exit()
print(-1)