# pack, grid, place

import tkinter as tk

windows = tk.Tk()
windows.geometry("300x300")

labels_1 = tk.Label(text= "Hello there", bg="black", fg="white", font="Verdana 22")
labels_1.pack(side = "left")  #top,left,right,bottom

labels_2 = tk.Label(text= "How are you doing?", bg="pink", fg="purple", font="Verdana 22")
labels_2.pack(side = "left")

labels_3 = tk.Label(text= "How's it going?", bg="pink", fg="purple", font="Verdana 22")
labels_3.pack(fill ="x") #x, y

labels_4 = tk.Label(text= "okey", bg="pink", fg="black", font="Verdana 22")
labels_4.pack(expand="yes") #yes, no

windows.mainloop()

#grid
windows_2 = tk.Tk()
windows_2.geometry("300x300")

p2e1 = tk.Label(text= "name", bg="black", fg="white", font="Verdana 22")
p2e1.grid(row=0, column=0)

p2e2 = tk.Label(text= "surname", bg="black", fg="white", font="Verdana 22")
p2e2.grid(row=2, column=1)

windows_2.mainloop()


#place
windows_3 = tk.Tk()
windows_3.geometry("300x300")

p3e1 = tk.Label(text= "self-confidence", bg="green", fg="white", font="Verdana 22")
p3e1.place(x=20, y=20)

p3e2 = tk.Label(text= "you can do it", bg="green", fg="white", font="Verdana 22")
p3e2.place(x=150, y=20)

windows_3.mainloop()
