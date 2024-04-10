r = int(input())
for i in range(r):
    if r % 2 == 0:
        print("* " * (r // 2))
        print(" *" * (r // 2))
    else:
        print("* " * ((r // 2) + 1))
        print(" *" * (r // 2))