n = int(input())
a, b = 0, 0
def fib(n):
    global a
    if n == 1 or n == 2:
        a += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
f = [0] * (n + 1)
def fibonacci(n):
    global b
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        b += 1
    return f[n]
fib(n)
fibonacci(n)
print(a, b)