from copy import deepcopy

#kelas yang merepresentasikan simpul dari graf
class Node:
    def __init__(self,idx,tabHn,tabNama):
        self.idx = idx                          #indeks dari simpul
        self.name = findName(idx,tabNama)       #nama simpul
        self.track = "null"                     #nama-nama simpul yang dikunjungi sebelum simpul ini dikunjungi
        self.f = 0                              #nilai f(n)
        self.g = 0                              #nilai g(n)
        self.h = tabHn[int(self.idx)]

    #mengembalikan hasil copy dari node
    def copy(self):
        return deepcopy(self)

    #menampilkan info dari node
    def print(self):
        print("Nama     : " + self.name)
        print("Indeks   : " + str(self.idx))
        print("Jejak    : " + self.track)
        print("F(n)     : " + str(self.f))
        print("G(n)     : " + str(self.g))
        print("H(n)     : " + str(self.h) + '\n')

    #mendapatkan indeks parent dari node
    def getParent(self):
        idxs = self.track.split()
        return idxs[len(idxs) - 1]

    #mendapatkan string berupa urutan nama-nama dari simpul yang telah dilewati hingga mencapai simpul yang sekarang
    def getRekamJejak(self,tabNama):
        if self.track == "null":
            return "Tidak ada rekam jejak"
        ancestors = self.track.split()
        jejak = ""
        i = 0
        while i < len(ancestors):
            jejak += findName(int(ancestors[i]),tabNama) + " -> "
            i+=1
        jejak += self.name
        return jejak

    #mendapatkan list indeks dari urutan simpul yang telah dilewati hingga mencapai simpul yang sekarang
    def getListJejak(self):
        if self.track == "null":
            return []
        ancestors = self.track.split()
        listJejak = []
        for x in ancestors:
            listJejak.append(int(x))
        listJejak.append(self.idx)
        return listJejak

    #mendapatkan list indeks tetangga dari sebuah simpul node
    def getListAdjIdx(self,tabAdj):
        listAdj=[]
        numNode = len(tabAdj[0])
        for i in range(numNode):
            if (tabAdj[int(self.idx)][i]):
                if not self.isVisited(i):
                    listAdj.append(i)
        return listAdj

    #mendapatkan list simpul tetangga dari sebuah simpul node
    def getListAdjNode(self,tabAdj,tabNama,tabKoor):
        listAdj = self.getListAdjIdx(tabAdj)
        listNode = self.getListNextNode(listAdj,tabNama,tabKoor)
        return listNode

    #menambahkan indeks node ke dalam track dari simpul dan mengganti nama simpul dengan simpul selanjutnya
    def nextNode(self, nextIdx):
        temp = self.copy()
        if temp.track == "null":
            temp.track = str(temp.idx)
        else:  # node.track != "null"
            temp.track = temp.track + " " + str(temp.idx)
        temp.idx = nextIdx
        temp.name = findName(nextIdx)
        temp.g += getEuclideanDistance(temp.getParent(), nextIdx)
        temp.f = temp.g + temp.h
        return temp

    #mengembalikan list berisi Node yang merupakan hasil next dari simpul node terhadap indeks pada listIdx
    def getListNextNode(self, listIdx,tabNama, tabKoor):
        listNode = []
        for x in listIdx:
            temp = deepcopy(self)
            if temp.track == "null":
                temp.track = str(temp.idx)
            else:  #node.track != "null"
                temp.track = temp.track + " " + str(temp.idx)
            temp.idx = x
            temp.name = findName(x,tabNama)
            temp.g += getEuclideanDistance(temp.getParent(), x, tabKoor)
            temp.f = temp.g + temp.h
            listNode.append(temp)
        return listNode

    def cleanListNode(self, listNode):
        for node in listNode:
            if node.f >= self.f:
                listNode.remove(node)

    #mengecek apakah simpul pada checkIdx sudah dikunjungi oleh simpul node atau belum
    def isVisited(self, checkIdx):
        if self.track == "null":
            return False
        else:
            idxs = self.track.split()
            for i in range(len(idxs)):
                if idxs[i] == str(checkIdx):
                    return True
            return False

    #memasukkan simpul apabila listNode kosong atau apabila simpul memiliki nilai f yang lebih kecil daripada elemen listNode
    def appendCheck(self,listNode):
        if len(listNode)== 0:
            listNode.append(self)
        else:
            if self.f < listNode[0].f:
                listNode.clear()
                listNode.append(self)
            #else: do nothing

#mendapatkan nama dari simpul sesuai dengan indeksnya
def findName(idx,tabNama):
    return tabNama[int(idx)]

#mendapatkan indeks dari simpul sesuai dengan namanya
def findIdx(name,tabNama):
    for i in range(len(tabNama)):
        if tabNama[i]==name:
            return i

#mendapatkan jarak euclidean antara simpul start dan simpul goal
def getEuclideanDistance(startIdx,goalIdx,tabKoor):
    diffX = abs(tabKoor[int(goalIdx)][0] - tabKoor[int(startIdx)][0])
    diffY = abs(tabKoor[int(goalIdx)][1] - tabKoor[int(startIdx)][1])
    result = (diffX**2 + diffY**2)**0.5
    #print("jarak dari " + str(startIdx) + " ke " + str(goalIdx) + " = " + str(result))
    return(result)

#mengisi tabHn dengan nilai heuristik yang dihitung berdasarkan jarak simpul ke simpul goal
def generateHn(goalIdx, tabHn, tabKoor):
    for nodeIdx in range(len(tabHn)):
        tabHn[nodeIdx] = getEuclideanDistance(nodeIdx, goalIdx,tabKoor)

#mengembalikan indeks dari node dengan f(n) terkecil
def getBestNodeIdx(listNode):
    idxmin = 0
    min = listNode[0].f
    for i in range(len(listNode)):
        if min>listNode[i].f:
            min=listNode[i].f
            idxmin=i
    return idxmin

#mengembalikan indeks dari simpul goal pada listNode, mengembalikan -1 bila simpul goal tidak ditemukan
def findGoalIdx(listNode, goalIdx):
    for i in range(len(listNode)):
        if int(listNode[i].idx) == int(goalIdx):
            return i
    #apabila tidak ditemukan
    return -1
