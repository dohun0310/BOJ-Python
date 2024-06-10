def matrix_mult(A, B, mod):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]
def matrix_pow(mat, power, mod):
    result = [[1, 0], [0, 1]]
    base = mat
    while power:
        if power % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        power //= 2
    return result
def fibonacci(n, mod=int(1e9) + 7):
    if n <= 1:
        return n
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1, mod)
    return result[0][0]
n = int(input())
print(fibonacci(n), n - 2)