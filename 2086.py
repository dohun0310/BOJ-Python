def matrix_multi(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % t, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % t], [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % t, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % t]]

def fibonacci(n):
    if n <= 0:
        return 0
    s = [[1, 0], [0, 1]]
    m = [[1, 1], [1, 0]]
    p = n - 1
    while p:
        if p % 2:
            s = matrix_multi(s, m)
        m = matrix_multi(m, m)
        p //= 2
    return s[0][0]

t = 10 ** 9
a, b = map(int, input().split())
print((fibonacci(b + 2) - fibonacci(a + 1)) % t)