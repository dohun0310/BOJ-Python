while True:
    nx, ny, w = map(float, input().split())
    if nx == 0 and ny == 0 and w == 0:
        break
    xi = sorted(map(float, input().split()))
    yi = sorted(map(float, input().split()))
    x, y = 0, 0
    for i in range(int(nx)):
        if xi[i] - x > w / 2:
            print("NO")
            break
        x = xi[i] + w / 2
    else:
        for i in range(int(ny)):
            if yi[i] - y > w / 2:
                print("NO")
                break
            y = yi[i] + w / 2
        else:
            if x >= 75 and y >= 100:
                print("YES")
            else:
                print("NO")