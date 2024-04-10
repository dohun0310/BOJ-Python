r = int(input())
for i in range(r * 5):
    if i < r:
        print("@@@@@" * r)
    elif r <= i < r * 3 + r:
        print("@" * r)
    else:
        print("@@@@@" * r)