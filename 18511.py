from itertools import product
n, m = map(int, input().split())
k = sorted(list(map(int, input().split())), reverse=True)
l = len(str(n))
while True:
    s = list(product(k, repeat=l))
    for i in s:
        p = int("".join(map(str, i)))
        if p <= n:
            print(p)
            exit()
    l -= 1