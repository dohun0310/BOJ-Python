r = int(input())
l = []
for i in range(r):
    n = int(input())
    l.append(n)
if l.count(1) < l.count(0):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")