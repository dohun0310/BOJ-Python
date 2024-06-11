s = 0
for i in [3, 2, 1]:
    n = input()
    if n not in ["FizzBuzz", "Fizz", "Buzz"]:
        s = int(n) + i
if s % 3 == 0 and s % 5 == 0:
    print("FizzBuzz")
elif s % 3 == 0:
    print("Fizz")
elif s % 5 == 0:
    print("Buzz")
else:
    print(s)