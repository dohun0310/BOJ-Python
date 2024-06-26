for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = [0] * n
    s[0] = l[0]
    for j in range(1, n):
        s[j] = max(s[j - 1] + l[j], l[j])
    print(max(s))