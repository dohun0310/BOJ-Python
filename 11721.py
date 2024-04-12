l = list(input())
for i in range(0, len(l), 10):
    print("".join(l[i:i + 10]))