c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
n = input()
for i in c:
    n = n.replace(i, "*")
print(len(n))