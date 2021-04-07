import tkinter as tk
import InputFile as i
import Node as n
import Main as m

from tkinter import StringVar

def submit(master, fileName, numNode, tabNama, tabKoor, tabAdj, start, finish):
    fileName = e1.get()
    str_out.set(fileName)
    i.inputFile(fileName,numNode, tabNama, tabKoor, tabAdj)

    print(tabNama[0])

    options = tk.StringVar(master)
    options.set("") # default value

    # Menampilkan pilihan tempat awal
    tk.Label(master, 
        text="Start : ").grid(row=4,column=0,padx=5,pady=10)

    om1 = tk.OptionMenu(master, options, *tabNama)
    om1.grid(row=4,column=1) 

    options2 = tk.StringVar(master)
    options2.set("") # default value

    # Menampilkan pilihan tempat akhir
    tk.Label(master, 
        text="Finish : ").grid(row=5,column=0,padx=5,pady=10)

    om1 = tk.OptionMenu(master, options2, *tabNama)
    om1.grid(row=5,column=1) 

    # Menampilkan tombol search
    tk.Button(master, 
          text='Search', 
          command = lambda : getSimpul(options,options2,start,finish,tabNama)).grid(row=6, 
                               column=1, 
                               sticky=tk.W, 
                               pady=4)

def getSimpul(options, options2, start, finish, tabNama):
    start = options.get()
    finish = options2.get()
    
    startIdx = n.findIdx(start,tabNama)
    goalIdx = n.findIdx(finish,tabNama)

    print(startIdx)
    print(goalIdx)
    #men-generate nilai h(n) berdasarkan simpul goal
    tabHn = [0 for i in range(numNode)]
    n.generateHn(goalIdx, tabHn)

    print(tabHn)

    #memulai pencarian jalur terpendek menggunakan algoritma A*
    # startNode = n.Node(startIdx, tabHn,tabNama)
    # resultNode = m.aStar(startIdx, goalIdx, [], [], startNode)

    # if resultNode != -1:
    #     resultNode.print()
    # else: #resultNode == -1
    #     print("Solusi tidak ditemukan")
    
    

# Inisiasi Variabel
fileName = "" 
numNode = 0 
tabNama = [""] 
tabKoor = [""]
tabAdj = [""]
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
         text="Penuntunmu",font=("Arial",25)).grid(row=0,column=2)
tk.Label(master, 
         text="\"Menuntunmu ke Jalan yang Benar dengan Cepat\"").grid(row=1,column=2)

e1 = tk.Entry(master)

e1.grid(row=3, column=1, padx=10)

tk.Button(master, 
          text='Submit', 
          command= lambda :submit(master, fileName, numNode, tabNama, tabKoor, tabAdj, start, finish)).grid(row=3, 
                               column=2, 
                               sticky=tk.W, 
                               pady=4)

# Menampilkan nama file yang dipilih
str_out=tk.StringVar(master)
str_out.set("File")

l2 = tk.Label(master,  textvariable=str_out, width=10 )  
l2.grid(row=3,column=2) 

# options = tk.StringVar(master)
# options.set("") # default value

# # Menampilkan pilihan tempat awal dan akhir
# tk.Label(master, 
#      text="Start : ").grid(row=4,column=0,padx=5,pady=10)

# om1 = tk.OptionMenu(master, options, *tabNama)
# om1.grid(row=4,column=1) 




# variable = StringVar(master)
# variable.set("")    # default value
# om1 = tk.OptionMenu(master,variable,*tabNama)

# tk.Label(master, 
#          text="Finish : ").grid(row=6,column=0,padx=5,pady=10)


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