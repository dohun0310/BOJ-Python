s = input()
for i in ["pi", "ka", "chu"]:
    s = s.replace(i, " ")
if len(s.rstrip()) == 0:
    print("YES")
else:
    print("NO")