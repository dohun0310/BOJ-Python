n = input()
l = ["U", "C", "P", "C"]
c = 0
for i in l:
    if i in n:
        c += 1
        n = n[n.index(i) + 1:]
    else:
        print("I hate UCPC")
        break
if c == 4:
    print("I love UCPC")