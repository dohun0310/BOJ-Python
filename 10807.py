n = input()
l = list(map(int, input().split()))
v = int(input())
g = 0
for i in l:
    if i == v:
        g += 1
print(g)