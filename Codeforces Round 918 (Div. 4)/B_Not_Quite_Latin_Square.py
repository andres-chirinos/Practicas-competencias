for _ in range(int(input())):
    letras = {"A","B","C"}
    m = [[x for x in input()] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if m[i][j] == "?":
                a = letras-set(m[i])
                b = letras-set([m[0][j],m[1][j],m[2][j]])
                if a==b:
                    print(list(a)[0])