n, m = map(int, input().split())
s = input()
for i in range(m):
    t = 0
    for j in input():
        if j in s and s[t] == j:
            t += 1
        if n == t:
            print("true")
            break
    else:
        print("false")