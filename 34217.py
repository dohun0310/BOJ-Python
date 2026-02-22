a, b = map(int, input().split())
c, d = map(int, input().split())
x, y = a + c, b + d
if x > y:
    print("Yongdap")
elif x < y:
    print("Hanyang Univ.")
else:
    print("Either")