d = {
    1967: "DavidBowie",
    1969: "SpaceOddity",
    1970: "TheManWhoSoldTheWorld",
    1971: "HunkyDory",
    1972: "TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars",
    1973: ["AladdinSane", "PinUps"],
    1974: "DiamondDogs",
    1975: "YoungAmericans",
    1976: "StationToStation",
    1977: ["Low", "Heroes"],
    1979: "Lodger",
    1980: "ScaryMonstersAndSuperCreeps",
    1983: "LetsDance",
    1984: "Tonight",
    1987: "NeverLetMeDown",
    1993: "BlackTieWhiteNoise",
    1995: "1.Outside",
    1997: "Earthling",
    1999: "Hours",
    2002: "Heathen",
    2003: "Reality",
    2013: "TheNextDay",
    2016: "BlackStar"
}
for i in range(int(input())):
    s, e = map(int, input().split())
    if s < 1967:
        s = 1967
    if e > 2016:
        e = 2016
    r = []
    for j in d:
        if s <= j <= e:
            if type(d[j]) == list:
                for k in d[j]:
                    r.append([j, k])
            else:
                r.append([j, d[j]])
    print(len(r))
    for j in r:
        print(*j)