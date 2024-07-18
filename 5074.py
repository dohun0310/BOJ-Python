while True:
    a, b = input().split()
    if a == "00:00" and b == "00:00":
        break
    h, m = int(a.split(":")[0]) + int(b.split(":")[0]), int(a.split(":")[1]) + int(b.split(":")[1])
    if h + (m // 60) >= 24:
        print(f"{((h + (m // 60)) % 24):02}:{(m % 60):02} +{(h + (m // 60)) // 24}")
    else:
        print(f"{((h + (m // 60)) % 24):02}:{(m % 60):02}")