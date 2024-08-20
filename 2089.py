n = int(input())
if n == 0:
    print(0)
    exit()
t = ""
while n != 0:
    if n % -2 != 0:
        t += "1"
        n = n // -2 + 1
    else:
        t += "0"
        n = n // -2
print(t[::-1])