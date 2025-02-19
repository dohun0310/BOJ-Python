n = int(input())
l = [[] for i in range(6)]
t = 1
for i in range(n):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
if 3 and 4 not in l[1] or len(l[1]) != 2:
    t = 0
elif 1 and 4 not in l[3] or len(l[3]) != 2:
    t = 0
elif 1 and 3 not in l[4] or len(l[4]) != 2:
    t = 0
if t:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")