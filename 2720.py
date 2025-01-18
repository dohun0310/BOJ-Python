for i in range(int(input())):
    c = int(input())
    a = c // 25
    c %= 25
    b = c // 10
    c %= 10
    print(a, b, c // 5, c % 5)