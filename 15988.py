l = [1, 2, 4, 7]
for i in range(int(input())):
    n = int(input())
    for i in range(len(l), n):
        l.append((l[-1] + l[-2] + l[-3]) % 1000000009)
    print(l[n - 1])