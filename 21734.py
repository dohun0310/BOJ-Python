s = list(input())
for i in s:
    a = sum(list(map(int, list(str(ord(i))))))
    print(i * a)