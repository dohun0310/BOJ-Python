n = int(input())
l = list(input())
m = [0] * 4
for i in range(n):
    if l[i] == "A":
        m[0] += 1
    elif l[i] == "C":
        m[1] += 1
    elif l[i] == "G":
        m[2] += 1
    elif l[i] == "T":
        m[3] += 1
r = 1
for i in m:
    r *= i
    r %= 1000000007
print(r)