import tkinter as tk
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
        tk.Label(master, 
         text="Jarak antara "+start+" dengan "+ finish +" adalah : "+str(resultNode.f)+" km").place(x=20,y=280)
    else: #resultNode == -1
        tk.Label(master, 
         text="Solusi tidak ditemukan").place(x=20,y=280)
        print("Solusi tidak ditemukan")
    
    

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