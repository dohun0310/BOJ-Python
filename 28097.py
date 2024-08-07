n = int(input())
l = sum(list(map(int, input().split()))) + (8 * (n - 1))
print(l // 24, l % 24)