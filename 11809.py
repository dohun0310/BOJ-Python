n = list(input())
m = list(input())
for i in range(min(len(n), len(m))):
    t = -i - 1
    if int(n[t]) > int(m[t]):
        m[t] = ""
    elif int(n[t]) < int(m[t]):
        n[t] = ""

if "".join(n) == "":
    print("YODA")
else:
    print(int("".join(n)))
if "".join(m) == "":
    print("YODA")
else:
    print(int("".join(m)))