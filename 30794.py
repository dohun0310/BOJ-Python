n, v = map(str, input().split())
n = int(n)
if v == "miss":
    print(0)
elif v == "bad":
    print(n * 200)
elif v == "cool":
    print(n * 400)
elif v == "great":
    print(n * 600)
elif v == "perfect":
    print(n * 1000)