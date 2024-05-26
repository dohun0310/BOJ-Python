import datetime
for i in range(3):
    hc, mc, sc, ht, mt, st = map(int, input().split())
    t = datetime.timedelta(hours=ht, minutes=mt, seconds=st) - datetime.timedelta(hours=hc, minutes=mc, seconds=sc)
    print(t.seconds // 3600, t.seconds % 3600 // 60, t.seconds % 60)