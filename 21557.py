n = int(input()) - 2
l = list(map(int, input().split()))
while n > 1:
    if l[0] > l[-1]:
        l[0] -= 1
    else:
        l[-1] -= 1
    n -= 1
print(max(l[0], l[-1]) - 1)