t = int(input())
a = list(map(int, input().split()))
m = [0] * 80001
s = 0
for i in range(len(m)):
    if i % 3 == 0 or i % 7 == 0:
        s += i
    m[i] = s
for i in a:
    print(m[i])