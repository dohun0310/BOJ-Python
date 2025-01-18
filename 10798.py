l = [""] * 5
for i in range(5):
    l[i] = input()
for i in range(15):
    for j in l:
        if i < len(j):
            print(j[i], end="")
        else:
            continue