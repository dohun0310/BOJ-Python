l = [0] * 9
for i in range(9):
    l[i] = int(input())
if sum(l) == 100:
    print(*l, sep="\n")
else:
    for i in range(9):
        for j in range(i + 1, 9):
            if sum(l) - l[i] - l[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(l[k])
                exit()