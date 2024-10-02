n = int(input())
l = list(map(int, input().split()))
if l.count(0) >= n / 2:
    print("INVALID")
elif l.count(1) > l.count(-1):
    print("APPROVED")
else:
    print("REJECTED")