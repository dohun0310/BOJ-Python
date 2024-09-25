c = 0
while True:
    s = input()
    if s == "고무오리 디버깅 끝":
        if c == 0:
            print("고무오리야 사랑해")
        else:
            print("힝구")
        break
    if s == "문제":
        c += 1
    elif s == "고무오리":
        if c == 0:
            c += 2
        else:
            c -= 1