import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx

import InputFile as i
import Node as n
import Main as m

from tkinter import StringVar

def submit(master, fileName, numNode, tabNama, tabKoor, tabAdj, start, finish):
    fileName = e1.get()
    str_out.set(fileName)
    i.inputFile(fileName, numNode, tabNama, tabKoor, tabAdj)

    options = tk.StringVar(master)
    options.set("") # default value

    # Menampilkan pilihan tempat awal
    tk.Label(master, 
        text="Start : ").place(x=20,y=150)

    om1 = tk.OptionMenu(master, options, *tabNama)
    om1.place(x=70,y=147)

    options2 = tk.StringVar(master)
    options2.set("") # default value

    # Menampilkan pilihan tempat akhir
    tk.Label(master, 
        text="Finish : ").place(x=20,y=190)

    om1 = tk.OptionMenu(master, options2, *tabNama)
    om1.place(x=70,y=187) 

    # Menampilkan tombol search
    tk.Button(master, 
          text='Search', 
          command = lambda : getSimpul(options,options2,start,finish,tabNama,tabKoor,tabAdj)).place(x=20,y=230) 

def getSimpul(options, options2, start, finish, tabNama, tabKoor, tabAdj):
    start = options.get()
    finish = options2.get()
    
    startIdx = n.findIdx(start,tabNama)
    goalIdx = n.findIdx(finish,tabNama)

    numNode = len(tabNama)
    
    #men-generate nilai h(n) berdasarkan simpul goal
    tabHn = [0 for i in range(numNode)]
    n.generateHn(goalIdx, tabHn, tabKoor)
    
    #memulai pencarian jalur terpendek menggunakan algoritma A*
    startNode = n.Node(startIdx, tabHn,tabNama)
    resultNode = m.aStar(startIdx, goalIdx, [], [], startNode,tabAdj,tabNama,tabKoor)

    if resultNode != -1:
        resultNode.print()
        print(resultNode.getRekamJejak(tabNama))
        print(resultNode.getListJejak())
        tk.Label(master,
              text="Jarak antara "+start+"dengan "+ finish +" adalah: "+str(resultNode.f)+" km").place(x=20,y=280)
        tk.Label(master,
                 text="Jalur koneksi: " + str(resultNode.getRekamJejak(tabNama))).place(
            x=20, y=310)

        tk.Label(master,
                 text="Legenda : ").place(
            x=20, y=350)

        for i in range(len(tabNama)):
            tk.Label(master,
                    text=str(i) +" : " +str(tabNama[i])).place(
                x=20, y=370+i*20)

        jejak = resultNode.getListJejak()
        
        visualisasi(tabNama, tabKoor, tabAdj,jejak)
    else: #resultNode == -1
        tk.Label(master, 
         text="Solusi tidak ditemukan.").place(x=20,y=280)
        print("Solusi tidak ditemukan.")
    
def visualisasi(tabNama, tabKoor, tabAdj, jejak) :
    G = nx.Graph()

    for i in range(len(tabNama)):
        G.add_node(i,pos=(tabKoor[i][0],tabKoor[i][1]))

    for i in range(len(tabNama)):
        for j in range(len(tabNama)):
            if (tabAdj[i][j]):
                G.add_edge(i,j,color='b')

    G.add_edge(0,1,color='r')
    pos = nx.get_node_attributes(G,'pos')

    labels ={}
    for i in range(len(tabNama)) :
        labels[i] = i

    colors = [G[u][v]['color'] for u,v in G.edges()]
    nx.draw_networkx_nodes(G,pos,node_size=500)
    nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
    nx.draw_networkx_labels(G,pos,labels,font_size=16)

    for i in range(len(jejak)-1):
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(jejak[i],jejak[i+1])],
            width=8,
            alpha=0.5,
            edge_color="r",)


    plt.show()
    

# Inisiasi Variabel
fileName = ""
numNode = 0 
tabNama = [] 
tabKoor = []
tabAdj = []
start = ""
finish = ""

# Inisiasi
master = tk.Tk()

# Set judul window
master.title("Penuntumu")
 
# Set ukuran window
master.geometry("550x600")

# Layout GUI
tk.Label(master, 
         text="Penuntunmu",font=("Arial",25)).place(x=170,y=10)
tk.Label(master, 
         text="\"Menuntunmu ke Jalan yang Benar dengan Cepat\"").place(x=120,y=60)

e1 = tk.Entry(master)

e1.place(x=20,y=103)

tk.Button(master, 
          text='Submit', 
          command= lambda :submit(master, fileName, numNode, tabNama, tabKoor, tabAdj, start, finish)).place(x=170,y=100)

# Menampilkan nama file yang dipilih
str_out=tk.StringVar(master)
str_out.set("File")

l2 = tk.Label(master,  textvariable=str_out, width=10 )  
l2.place(x=230,y=103)




# tk.Button(master, 
#           text='Quit', 
#           command=master.quit).grid(row=3, 
#                                     column=0, 
#                                     sticky=tk.W, 
#                                     pady=4)
# tk.Button(master, 
#           text='Show', command=show_entry_fields).grid(row=3, 
#                                                        column=1, 
#                                                        sticky=tk.W, 
#                                                        pady=4)

tk.mainloop()