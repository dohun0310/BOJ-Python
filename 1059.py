l = int(input())
s = list(map(int, input().split()))
n = int(input())
s.sort()
if n in s:
    print(0)
else:
    max = 0
    min = 0
    for i in s:
        if i < n:
            min = i
        elif i > n and max == 0:
            max = i
    max -= 1
    min += 1
    print((n - min) * (max - n + 1) + (max - n))