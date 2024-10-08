n = int(input())
l = [0] + list(map(int,input().split()))
x = int(input())
for i in range(n):
    if (i + 1) * x == l[i + 1] or (l[i] < i * x and l[i + 1] > (i + 1) * x) or (l[i] > i * x and l[i + 1] < (i + 1) * x):
        print("T")
        exit()
print("F")