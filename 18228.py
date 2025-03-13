n = int(input())
l = input()
a, b = list(map(int, l.split("-1")[0].split())), list(map(int, l.split("-1")[1].split()))
print(min(a) + min(b))