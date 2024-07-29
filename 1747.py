n = int(input())
while True:
    if n == 1:
        n += 1
        continue
    if str(n) == str(n)[::-1]:
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                break
        else:
            print(n)
            break
    n += 1