r = int(input())
for i in range(r * 5):
    if i < (r * 4):
        print("@" * r)
    else:
        print("@" * (r * 5))