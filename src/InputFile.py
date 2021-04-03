#melakukan pembacaan file
#filename = input("Masukkan nama file test: ")
#f = open("../test/" + filename, "r")
f = open("../test/test1.txt","r")
lines = f.readlines()

#menyimpan banyaknya simpul ke dalam numNode
numNode = int(lines[0])

#menyimpan data koordinat dan nama simpul ke dalam tabNode
tabNode = [["*" for j in range(2)] for i in range(numNode)]
for i in range(1,numNode+1):
    words = lines[i].split()
    tabNode[i-1][0] = words[0]
    tabNode[i-1][1] = words[1]
print(tabNode)

#menyimpan data matriks ketetanggaan ke dalam tabAdj
tabAdj = [["*" for j in range(numNode)] for i in range(numNode)]
for i in range(numNode+1, numNode*2+1):
    numbers = lines[i].split()
    for j in range(numNode):
        tabAdj[i-numNode-1][j]=numbers[j]
print(tabAdj)
