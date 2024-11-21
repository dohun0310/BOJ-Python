s = input()
c = 0
for i in s:
    if i.islower():
        c += ord(i) - 96
    else:
        c += ord(i) - 38
for i in range(2, c):
    if c % i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")