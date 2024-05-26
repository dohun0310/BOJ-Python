import datetime
yt, mt, dt = map(int, input().split())
yd, md, dd = map(int, input().split())
t = datetime.date(yt, mt, dt)
d = datetime.date(yd, md, dd)
if d >= t.replace(t.year + 1000):
    print("gg")
else:
    print(f"D-{(d - t).days}")