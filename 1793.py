l = [1, 1, 3] + [0] * 248
while True:
    try:
        n = int(input())
        for i in range(3, n + 1):
            l[i] = 2 * l[i - 2] + l[i - 1]
        print(l[n])
    except:
        break