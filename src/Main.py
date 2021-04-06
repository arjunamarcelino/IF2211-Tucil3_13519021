import Node as n

def aStar(startIdx, goalIdx, initListHold, initListGoal,initCurrNode):
    listHold = initListHold.copy()
    listGoal = initListGoal.copy()
    currNode = initCurrNode.copy()

    #mengembalikan simpul start apabila startIdx == goalIdx
    if startIdx == goalIdx:
        return currNode

    #mengembalikan currNode apabila solusi sudah ditemukan
    if len(listHold) == 0 and currNode.idx != startIdx:
        if len(listGoal) == 0:
            print("Solusi tidak ditemukan.")
            return currNode
        else:
            idxBest = n.getBestNodeIdx(listGoal)
            return listGoal[idxBest]

    listNode = currNode.getListAdjNode()
    foundIdx = n.findGoalIdx(listNode,goalIdx)
    if foundIdx == -1:
        idxBest = n.getBestNodeIdx(listNode)
        currNode = listNode[idxBest].copy()
        del listNode[idxBest]
        listHold += listNode
        return aStar(startIdx,goalIdx,listHold,listGoal,currNode)
    else:
        tempNode = listNode[foundIdx].copy()
        listNode.remove(listNode[foundIdx])
        listHold += listNode
        tempNode.cleanListNode(listHold)
        listGoal.append(tempNode)
        if (len(listHold) == 0):
            return tempNode
        else:
            currNode = listHold[0].copy()
            listHold.remove(listHold[0])
            return aStar(startIdx,goalIdx,listHold,listGoal,currNode)


if __name__ == '__main__':
    numNode = n.numNode
    tabHn = [0 for i in range(numNode)]
    listEmpty = []
    startIdx = input("Masukkan indeks simpul awal: ")
    goalIdx = input("Masukkan indeks simpul tujuan: ")
    n.generateHn(goalIdx, tabHn)
    currNode = n.Node(startIdx, tabHn)
    resultNode = aStar(startIdx, goalIdx, listEmpty, listEmpty, currNode)
    resultNode.print()