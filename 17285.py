s = input()
t = ord(s[0]) ^ ord("C")
a = ""
for i in s:
    a += chr(ord(i) ^ t)
print(a)