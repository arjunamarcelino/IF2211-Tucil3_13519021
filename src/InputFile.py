#melakukan pembacaan file
#filename = input("Masukkan nama file test: ")
#f = open("../test/" + filename, "r")
f = open("../test/testnyoba.txt","r")
lines = f.readlines()

#menyimpan banyaknya simpul ke dalam numNode
numNode = int(lines[0])

#menyimpan data nama simpul ke dalam tabNama
tabNama = ['*' for i in range(numNode)]
for i in range(1,numNode+1):
    tabNama[i-1] = lines[i]
    tabNama[i-1]=tabNama[i-1].replace('\n','')

#menyimpan data koordinat ke dalam tabKoor
tabKoor = [[0.0 for j in range(2)] for i in range(numNode)]
for i in range(numNode+1,numNode*2+1):
    words = lines[i].split()
    tabKoor[i-numNode-1][0] = float(words[0])
    tabKoor[i-numNode-1][1] = float(words[1])

#menyimpan data matriks ketetanggaan ke dalam tabAdj
tabAdj = [[False for j in range(numNode)] for i in range(numNode)]
for i in range(numNode*2+1, numNode*3+1):
    numbers = lines[i].split()
    for j in range(numNode):
        if numbers[j] == "1":
            tabAdj[i-numNode*2-1][j] = True















