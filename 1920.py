a = input()
n = list(map(int, input().split()))
b = input()
m = list(map(int, input().split()))
for i in m:
    if i in n:
        print(1)
    else:
        print(0)