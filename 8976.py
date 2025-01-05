import sys
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
l = [["x"] * 10] + [["x"] + list(sys.stdin.readline().strip()) + ["x"] for i in range(8)] + [["x"] * 10]
s = 0
for i in range(1, 9):
    for j in range(1, 9):
        if l[i][j] != ".":
            continue
        t = 0
        for k in range(8):
            c = 0
            x = i + dx[k]
            y = j + dy[k]
            while l[x][y] == "W":
                x += dx[k]
                y += dy[k]
                c += 1
            if l[x][y] == "B":
                t += c
        s = max(s, t)
print(s)