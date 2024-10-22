n = int(input())
s = list(map(int, input().split()))
s.sort()
print(n - 1 + s[-1])