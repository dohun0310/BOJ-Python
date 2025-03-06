for i in range(int(input())):
    n = int(input())
    for j in range(2, 1000001):
        if n % j == 0:
            print("NO")
            break
    else:
        print("YES")