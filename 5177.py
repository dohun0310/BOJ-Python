import sys
import re
for i in range(int(input())):
    a = input()
    b = input()
    a = a.upper()
    b = b.upper()
    a = re.sub("[\[{]", "(", a)
    b = re.sub("[\[{]", "(", b)
    a = re.sub("[\]}]", ")", a)
    b = re.sub("[\]}]", ")", b)
    a = re.sub(",", ";", a)
    b = re.sub(",", ";", b)
    a = re.sub("\s+", " ", a)
    b = re.sub("\s+", " ", b)
    a = re.sub("\s?\(\s?", "(", a)
    a = re.sub("\s?\)\s?", ")", a)
    a = re.sub("\s?\.\s?", ".", a)
    a = re.sub("\s?;\s?", ";", a)
    a = re.sub("\s?:\s?", ":", a)
    b = re.sub("\s?\(\s?", "(", b)
    b = re.sub("\s?\)\s?", ")", b)
    b = re.sub("\s?\.\s?", ".", b)
    b = re.sub("\s?;\s?", ";", b)
    b = re.sub("\s?:\s?", ":", b)
    sys.stdout.write("Data Set %d: %s\n\n" % (i + 1, "equal" if a == b else "not equal"))