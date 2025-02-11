def back(a):
    for i in range(1, a // 2 + 1):
        if s[-i:] == s[-2 * i:-i]:
            return -1
    if a == n:
        for i in range(n):
            print(s[i], end="")
        return 0
    for i in "123":
        s.append(i)
        if back(a + 1) == 0:
            return 0
        s.pop()
n = int(input())
s = []
back(0)