for i in range(int(input())):
    s = input().lower()
    l = []
    for j in range(ord("a"), ord("z") + 1):
        if chr(j) not in s:
            l.append(chr(j))
    if l:
        print("missing ", *l, sep="")
    else:
        print("pangram")