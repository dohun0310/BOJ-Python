while True:
    try:
        a, b, c = map(int, input().split())
        l = [abs(a - b), abs(b - c)]
        print(max(l) - 1)
    except:
        break