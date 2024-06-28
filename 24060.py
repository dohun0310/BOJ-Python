def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
def merge(A, p, q, r):
    global c, s
    i, j, t, tmp = p, q + 1, 1, []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            t += 1
            i += 1
        else:
            tmp.append(A[j])
            t += 1
            j += 1
    while i <= q:
        tmp.append(A[i])
        t += 1
        i += 1
    while j <= r:
        tmp.append(A[j])
        t += 1
        j += 1
    i, t = p, 0
    while i <= r:
        A[i] = tmp[t]
        c += 1
        if c == k:
            s = A[i]
            break
        i += 1
        t += 1
n, k = map(int, input().split())
l = list(map(int, input().split()))
c, s = 0, -1
merge_sort(l, 0, n - 1)
print(s)