n = int(input())
b = bin(n)[2:].zfill(32)
x = ""
for i in range(32):
  x += "1" if b[i] == "0" else "0"
y = bin(int(x,2)+1)[2:]
a = 0
for i in range(32):
  if y[i] != b[i]:
    a += 1
print(a)