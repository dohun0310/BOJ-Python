n = input()
l = list(map(int, input().split()))
c = sum(l)
a = 0
for i in l:
    c -= i
    a = (a + i * c) % 1000000007
print(a)