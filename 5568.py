from itertools import permutations
n = int(input())
k = int(input())
l = [""] * n
for i in range(n):
    l[i] = input()
s = set()
for i in permutations(l, k):
    s.add("".join(i))
print(len(s))