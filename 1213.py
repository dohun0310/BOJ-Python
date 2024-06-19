from collections import Counter
w = input()
l = sorted(list(w))
c = Counter(l)
a, o = 0, ""
for i in c:
    if c[i] % 2 == 1:
        a += 1
        o += i
    if a > 1:
        print("I'm Sorry Hansoo")
        exit()
s = ""
for i in range(0, len(w), 2):
    if c[l[i]] % 2 == 1:
        c[l[i]] -= 1
    else:
        s += l[i]
t = s[::-1]
s += o
s += t
print(s)