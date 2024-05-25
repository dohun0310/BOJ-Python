n = input()
f = int(input())
s = ""
for i in range(int(n[0:len(n) - 2]) * 100, int(n[0:len(n) - 2]) * 100 + 99):
    if i % f == 0:
        s = str(i)
        break
print(s[-2:])