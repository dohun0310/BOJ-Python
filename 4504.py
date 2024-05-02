n = int(input())
i = int(input())
while True:
    if i % n == 0:
        print("%s is a multiple of %s." % (i, n))
    else:
        print("%s is NOT a multiple of %s." % (i, n))
    i = int(input())
    if i == 0:
        break