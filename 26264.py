n = int(input())
s = input()
b = s.count("bigdata")
s = abs(n - b)
if b == s:
    print("bigdata? security!")
elif b > s:
    print("bigdata?")
else:
    print("security!")