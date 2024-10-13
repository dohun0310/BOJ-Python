d = {" ": 0, **{chr(i): i - 64 for i in range(65, 91)}, **{chr(i): i - 70 for i in range(97, 123)}}
n = int(input())
l = sorted(list(map(int, input().split())))
m = input()
s = sorted([d[i] for i in m])
if l == s:
    print("y")
else:
    print("n")