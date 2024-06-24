n = int(input())
s = list(map(int, input().split()))
for i in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b, n + 1, b):
            s[i - 1] = abs(s[i - 1] - 1)
    else:
        b -= 1
        s[b] = abs(s[b] - 1)
        for i in range(1, min(n - b, b + 1)):
            if s[b - i] == s[b + i]:
                s[b - i] = abs(s[b - i] - 1)
                s[b + i] = abs(s[b + i] - 1)
            else:
                break
for i in range(n):
    print(s[i], end=" ")
    if (i + 1) % 20 == 0:
        print()