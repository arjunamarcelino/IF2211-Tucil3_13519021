#melakukan pembacaan file
#filename = input("Masukkan nama file test: ")
#f = open("../test/" + filename, "r")
f = open("../test/test1.txt","r")
lines = f.readlines()

#menyimpan banyaknya simpul ke dalam numNode
numNode = int(lines[0])

#menyimpan data nama simpul ke dalam tabNama 
tabNama = ['*' for i in range(numNode)]
for i in range(1,numNode+1):
    tabNama[i-1] = lines[i]
    tabNama[i-1]=tabNama[i-1].replace('\n','')
print(tabNama)

#menyimpan data koordinat ke dalam tabKoor
tabKoor = [[0.0 for j in range(2)] for i in range(numNode)]
for i in range(numNode+1,numNode*2+1):
    words = lines[i].split()
    tabKoor[i-numNode-1][0] = float(words[0])
    tabKoor[i-numNode-1][1] = float(words[1])
print(tabKoor)

#menyimpan data matriks ketetanggaan ke dalam tabAdj
tabAdj = [[False for j in range(numNode)] for i in range(numNode)]
for i in range(numNode*2+1, numNode*3+1):
    numbers = lines[i].split()
    for j in range(numNode):
        if numbers[j] == "1":
            tabAdj[i-numNode*2-1][j] = True
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
    diffX = abs(tabKoor[int(goalIdx)][0] - tabKoor[int(startIdx)][0])
    diffY = abs(tabKoor[int(goalIdx)][1] - tabKoor[int(startIdx)][1])
    result = (diffX**2 + diffY**2)**0.5
    #print("jarak dari " + str(startIdx) + " ke " + str(goalIdx) + " = " + str(result))
    return(result)

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

#mendapatkan nilai g(n) dari simpul node
def countGn(node):
    if node.track == "null":
        return 0
    else:
        idxs = node.track.split()
        sum = getEuclideanDistance(node.idx, idxs[len(idxs)-1])
        for i in range(len(idxs)-1,0,-1):
            sum+=getEuclideanDistance(idxs[i],idxs[i-1])
        return sum

'''
node = Node(4)
addParent(node,3)
addParent(node,2)
addParent(node,0)
print(node.track)
gn = countGn(node)
print("g(n) = " + str(gn))            
'''




