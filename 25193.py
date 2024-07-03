n = int(input())
s = input()
c = s.count("C")
print(c // (n - c + 1) + (1 if c % (n - c + 1) != 0 else 0))