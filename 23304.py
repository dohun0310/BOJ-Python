def akaraka(s):
    if s != s[::-1]:
        return "IPSELENTI"
    if len(s) == 1:
        return "AKARAKA"
    r = len(s) // 2
    if akaraka(s[:r]) == "AKARAKA" and akaraka(s[-r:]) == "AKARAKA":
        return "AKARAKA"
    return "IPSELENTI"
s = input()
print(akaraka(s))