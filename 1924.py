import datetime
m, d = map(int, input().split())
w = datetime.date(2007, m, d).weekday()
if w == 0:
    print("MON")
elif w == 1:
    print("TUE")
elif w == 2:
    print("WED")
elif w == 3:
    print("THU")
elif w == 4:
    print("FRI")
elif w == 5:
    print("SAT")
elif w == 6:
    print("SUN")