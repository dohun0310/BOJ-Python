s = input()
n = len(s) // 3
if s[:n] == s[n:2 * n]:
    print(s[:n])
else:
    print(s[2 * n:])