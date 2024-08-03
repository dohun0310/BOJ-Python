d = {"AA": "A", "AG": "C", "AC": "A", "AT": "G", "GA": "C", "GG": "G", "GC": "T", "GT": "A", "CA": "A", "CG": "T", "CC": "C", "CT": "G", "TA": "G", "TG": "A", "TC": "G", "TT": "T"}
n = int(input())
s = list(input())
for i in range(n - 1)[::-1]:
    s[i] = d[s[i] + s[i + 1]]
    s[i + 1] = ""
print(s[0])