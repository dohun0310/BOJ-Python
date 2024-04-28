l = [0] * 10
n = input()
for i in n:
    if i == "6" or i == "9":
        if l[6] <= l[9]:
            l[6] += 1
        else:
            l[9] += 1
    else:
        l[int(i)] += 1
print(max(l))