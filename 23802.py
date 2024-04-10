r = int(input())
for i in range(r * 5):
    if i < r:
        print("@" * (r * 5))
    else:
        print("@" * r)