def inputFile(fileName, numNode, tabNama, tabKoor, tabAdj):
    f = open("../test/" + fileName, "r")
    lines = f.readlines()

    tabNama.clear()
    tabKoor.clear()
    tabKoor.clear()

    #menyimpan banyaknya simpul ke dalam numNode
    numNodeNew = int(lines[0])

    #menyimpan data nama simpul ke dalam tabNama
    tabNamaNew = ['*' for i in range(numNodeNew)]
    for i in range(1,numNodeNew+1):
        tabNamaNew[i-1] = lines[i]
        tabNamaNew[i-1] = tabNamaNew[i-1].replace('\n','')

    #menyimpan data koordinat ke dalam tabKoor
    tabKoorNew = [[0.0 for j in range(2)] for i in range(numNodeNew)]
    for i in range(numNodeNew+1,numNodeNew*2+1):
        words = lines[i].split()
        tabKoorNew[i-numNodeNew-1][0] = float(words[0])
        tabKoorNew[i-numNodeNew-1][1] = float(words[1])

    #menyimpan data matriks ketetanggaan ke dalam tabAdj
    tabAdjNew = [[False for j in range(numNodeNew)] for i in range(numNodeNew)]
    for i in range(numNodeNew*2+1, numNodeNew*3+1):
        numbers = lines[i].split()
        for j in range(numNode):
            if numbers[j] == "1":
                tabAdjNew[i-numNodeNew*2-1][j] = True

    tabNama += tabNamaNew
    tabKoor += tabKoorNew
    tabAdj += tabAdjNew