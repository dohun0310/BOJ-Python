while True:
    n = int(input())
    if n == -1:
        break
    p = []
    for i in range(1, n):
        if n % i == 0:
            p.append(i)
    if sum(p) == n:
        print(f"{n} = ", end="")
        print(*p, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")