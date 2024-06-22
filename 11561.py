t = int(input())
for i in range(t):
    n = int(input())
    a, b = 1, int(2 * (n ** 0.5)) + 1
    while a <= b:
        m = (a + b) // 2
        if (m * (m + 1)) // 2 <= n:
            a = m + 1
        else:
            b = m - 1
    print(b)