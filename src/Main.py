import Node as n

def aStar(startIdx, goalIdx, initListHold, initListGoal,initCurrNode, tabAdj,tabNama,tabKoor):
    listHold = initListHold.copy()      #menyimpan list simpul yang masih berpotensi untuk menghasilkan solusi terbaik
    listGoal = initListGoal.copy()      #menyimpan simpul goal terbaik apabila ditemukan (list dengan maks 1 elemen)
    currNode = initCurrNode.copy()      #menyimpan simpul yang saat ini sedang diperiksa

    #mengembalikan simpul start apabila startIdx == goalIdx
    if startIdx == goalIdx:
        print("Simpul awal sama dengan simpul akhir.")
        return currNode

    #melanjutkan pemeriksaan terhadap simpul-simpul tetangga dari currNode
    listAdjNode = currNode.getListAdjNode(tabAdj,tabNama,tabKoor)
    if len(listAdjNode) == 0:

        #apabila tidak ditemukan simpul tetangga, pemeriksaan dilakukan terhadap simpul yang di-hold
        if len(listHold) > 0:
            currNode = listHold[0].copy()
            listHold.remove(listHold[0])
            return aStar(startIdx, goalIdx, listHold, listGoal, currNode,tabAdj,tabNama,tabKoor)

        #apabila tidak ditemukan simpul tetangga dan simpul yang di-hold, mengembalikan elemen pertama listGoal
        if len(listGoal) > 0:
            return listGoal[0]

        #apabila tidak ditemukan simpul tetangga, simpul yang di-hold, dan simpul goal, maka solusi tidak ditemukan
        return -1       #mengembalikan kode error -1

    #mencari apakah ditemukan simpul goal pada listAdjNode
    foundIdx = n.findGoalIdx(listAdjNode,goalIdx)
    if foundIdx == -1:
        #apabila tidak ditemukan, dilakukan pemeriksaan terhadap simpul dengan f(n) terkecil
        idxBest = n.getBestNodeIdx(listAdjNode)
        currNode = listAdjNode[idxBest].copy()
        del listAdjNode[idxBest]
        listHold += listAdjNode
        return aStar(startIdx,goalIdx,listHold,listGoal,currNode,tabAdj,tabNama,tabKoor)

    else:
        #simpul goal ditemukan
        goalNode = listAdjNode[foundIdx].copy()
        listAdjNode.remove(listAdjNode[foundIdx])

        #memasukkan simpul tetangga lain ke dalam listHold
        listHold += listAdjNode

        #menghapus simpul-simpul yang di-hold dan memiliki nilai f(n) >= nilai f(n) simpul goal
        goalNode.cleanListNode(listHold)

        #memperbaharui listGoal apabila goalNode lebih efektif
        goalNode.appendCheck(listGoal)

        if len(listHold) == 0:
            #apabila tidak ada lagi simpul yang di-hold, mengembalikan goalNode
            return listGoal[0]

        else:
            #apabila masih ada, dilakukan pemeriksaan terhadap elemen pertama listHold
            currNode = listHold[0].copy()
            listHold.remove(listHold[0])
            return aStar(startIdx,goalIdx,listHold,listGoal,currNode,tabAdj,tabNama,tabKoor)
