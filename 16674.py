d = {2: 0, 0: 0, 1: 0, 8: 0}
for i in input():
    try:
        d[int(i)] += 1
    except:
        print(0)
        exit()
if d[2] != 0 and d[0] !=0 and d[1] != 0 and d[8] != 0:
    if d[2] == d[0] == d[1] == d[8]:
        print(8)
    else:
        print(2)
else:
    print(1)