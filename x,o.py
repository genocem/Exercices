import sys


def affichage(n):
    for o in range(3):
        for h in range(3):
            print(n[h][o], " ", end='')
        print()


def verification(t, win):
    for b in range(3):
        if t[b][0] == t[b][1] == t[b][2] and t[b][0] != "-":
            print(win)
            exit()
        elif t[0][b] == t[1][b] == t[2][b] and t[0][b] != "-":
            print(win)
            exit()
        elif t[0][0] == t[1][1] == t[2][2] and t[0][0] != "-":
            print(win)
            exit()


m = [["-"]*3 for i in range(3)]
affichage(m)
w = 0
while w == 0:
    p1x = int(input("Xx="))
    p1y = int(input("Xy="))
    w1 = "joueur 1 a gagner"
    while m[p1x][p1y] == "X" or m[p1x][p1y] == "O":
        print("no")
        p1x = int(input("Xx="))
        p1y = int(input("Xy="))
    m[p1x][p1y] = "X"
    affichage(m)
    verification(m, w1)

    p2x = int(input("Ox="))
    p2y = int(input("Oy="))
    w2 = "joueur 2 a gagner"
    while m[p2x][p2y] == "X" or m[p2x][p2y] == "O":
        print("no")
        p2x = int(input("Ox="))
        p2y = int(input("Oy="))
    m[p2x][p2y] = "O"
    affichage(m)
    verification(m, w2)
