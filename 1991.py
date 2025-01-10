import sys
def preorder(n):
    if n == ".":
        return
    print(n, end="")
    preorder(d[n][0])
    preorder(d[n][1])
def inorder(n):
    if n == ".":
        return
    inorder(d[n][0])
    print(n, end="")
    inorder(d[n][1])
def postorder(n):
    if n == ".":
        return
    postorder(d[n][0])
    postorder(d[n][1])
    print(n, end="")
d = {}
for i in range(int(sys.stdin.readline())):
    r, a, b = map(str, sys.stdin.readline().split())
    d[r] = [a, b]
preorder("A")
print()
inorder("A")
print()
postorder("A")