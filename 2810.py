n = int(input())
s = input()
a = s.count("S")
b = s.count("LL")
c = a + b + 1
if c >= n:
    print(n)
else:
    print(c)