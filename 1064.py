ax, ay, bx, by, cx, cy = map(int, input().split())
if (ax - bx) * (cy - by) == (ay - by) * (cx - bx):
    print(-1.0)
else:
    a, b, c = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5, ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5, ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5
    l = [a + b, a + c, b + c]
    print((max(l) - min(l)) * 2)