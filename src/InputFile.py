#melakukan pembacaan file
#filename = input("Masukkan nama file test: ")
#f = open("../test/" + filename, "r")
f = open("../test/test1.txt","r")
lines = f.readlines()

#menyimpan banyaknya simpul ke dalam numNode
numNode = int(lines[0])

#menyimpan data nama simpul ke dalam tabNama dan koordinat ke dalam tabKoor
tabNama = ["*" for i in range(numNode)]
tabKoor = [[0.0 for j in range(2)] for i in range(numNode)]
for i in range(1,numNode+1):
    words = lines[i].split()
    tabNama[i-1] = words[0]
    tabKoor[i-1][0] = float(words[1])
    tabKoor[i-1][1] = float(words[2])
#print(tabNama)
#print(tabKoor)

#menyimpan data matriks ketetanggaan ke dalam tabAdj
tabAdj = [[False for j in range(numNode)] for i in range(numNode)]
for i in range(numNode+1, numNode*2+1):
    numbers = lines[i].split()
    for j in range(numNode):
        if numbers[j] == "1":
            tabAdj[i-numNode-1][j] = True
#print(tabAdj)

#mendapatkan nama dari simpul sesuai dengan indeksnya
def findName(idx):
    return tabNama[idx]

#mendapatkan indeks dari simpul sesuai dengan namanya
def findIdx(name):
    for i in range(numNode):
        if tabNama[i]==name:
            return i

#mendapatkan jarak euclidean antara simpul start dan simpul goal
def getEuclideanDistance(startIdx,goalIdx):
    diffX = abs(tabKoor[goalIdx][0] - tabKoor[startIdx][0])
    diffY = abs(tabKoor[goalIdx][1] - tabKoor[startIdx][1])
    return((diffX**2 + diffY**2)**0.5)

#mengisi tabHn dengan nilai heuristik yang dihitung berdasarkan jarak simpul ke simpul goal
def generateHn(goalIdx, tabHn):
    for nodeIdx in range(numNode):
        tabHn[nodeIdx] = getEuclideanDistance(nodeIdx, goalIdx)

tabHn = [0.0 for i in range(numNode)]
generateHn(3,tabHn)
print(tabHn)

class Node:
    #kelas yang merepresentasikan simpul dari graf
    def __init__(self, idx):
        self.idx = idx
        self.name = findName(idx)       #nama simpul
        self.track = "null"             #nama-nama simpul yang dikunjungi sebelum simpul ini dikunjungi
        self.f = 0                      #nilai f(n)
        self.g = 0                      #nilai g(n)

#menambahkan parent ke dalam track dari simpul
def addParent(node, parentIdx):
    if node.track == "null":
        node.track = str(parentIdx)
    else: #node.track != "null"
        node.track = node.track + " " + str(parentIdx)

#mengecek apakah simpul pada checkIdx sudah dikunjungi oleh simpul node atau belum
def isVisited(node, checkIdx):
    if node.track == "null":
        return False
    else:
        idxs = node.track.split()
        for i in range(len(idxs)):
            if idxs[i] == str(checkIdx):
                return True
        return False
