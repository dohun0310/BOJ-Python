r = input()
s = input()
l = 0
for i in range(len(s)):
    l += (ord(s[i]) - 96) * (31 ** i)
print(l % 1234567891)