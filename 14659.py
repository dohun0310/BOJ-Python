n = int(input())
l = list(map(int, input().split()))
s, c, m = 0, 0, 0
for i in l:
    if s < i:
        c = 0
        s = i
    else:
        c += 1
        if m < c:
            m = c
print(m)