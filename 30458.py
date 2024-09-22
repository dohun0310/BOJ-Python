n = int(input()) // 2
s = input()
s = s[:n] + s[-n:]
for i in map(chr, range(97, 123)):
    if s.count(i) % 2:
        print("No")
        break
else:
    print("Yes")