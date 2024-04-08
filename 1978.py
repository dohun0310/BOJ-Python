r = input()
l = list(map(int, input().split()))
s = 0
for i in l:
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                s += 1
            else:
                break
print(s)