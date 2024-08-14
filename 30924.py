from random import shuffle
l = list(range(1, 10001))
shuffle(l)
while True:
    a = l.pop()
    print(f"? A {a}", flush = True)
    k = int(input())
    if k == 1:
        break
l = list(range(1, 10001))
shuffle(l)
while True:
    b = l.pop()
    print(f"? B {b}", flush = True)
    k = int(input())
    if k == 1:
        break
print(f"! {a + b}", flush = True)