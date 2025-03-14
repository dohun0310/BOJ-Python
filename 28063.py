n = int(input())
l = list(map(int, input().split()))
if n > 1:
    if l[0] in [1, n] and l[1] in [1, n]:
        print(2)
    elif 1 < l[0] < n and l[1] in [1, n] or l[0] in [1, n] and 1 < l[1] < n:
        print(3)
    else:
        print(4)
else:
    print(0)