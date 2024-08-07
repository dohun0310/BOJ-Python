for i in range(int(input())):
    n, d, a, b, f = map(float, input().split())
    print(int(n), "%.6f" % (d / (a + b) * f))