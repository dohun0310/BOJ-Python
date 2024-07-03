n = input()
if len(n) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    for i in range(len(n) - 1):
        if int(n[i]) - int(n[i + 1]) != int(n[0]) - int(n[1]):
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
    else:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")