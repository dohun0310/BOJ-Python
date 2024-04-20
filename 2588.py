a = int(input())
b = list(input())
for i in range(2, -1, -1):
    print(a * int(b[i]))
print(a * (int(b[0]) * 100 + int(b[1]) * 10 + int(b[2])))