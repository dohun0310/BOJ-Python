t = int(input())
for i in range(t):
    n = int(input())
    l = [0] * n
    for j in range(n):
        l[j] = int(input())
    if l.count(max(l)) > 1:
        print("no winner")
    elif max(l) > (sum(l) // 2):
        print("majority winner", l.index(max(l)) + 1)
    else:
        print("minority winner", l.index(max(l)) + 1)