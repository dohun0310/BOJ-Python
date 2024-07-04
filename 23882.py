def selection_sort(n, k, a):
    b = sorted(a)
    d = {}
    for i, j in enumerate(a):
        d[j] = i
    c = 0
    for i in range(n, -1, -1):
        if a[i] != b[i]:
            r = [a[i], b[i]]
            a[i], a[d[b[i]]] = a[d[b[i]]], a[i]
            d[r[0]], d[r[1]] = d[r[1]], d[r[0]]
            c += 1
            if c == k:
                print(*a)
    if c < k:
        print(-1)
n, k = map(int, input().split())
a = list(map(int, input().split()))
selection_sort(n - 1, k, a)