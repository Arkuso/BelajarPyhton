from tkinter import *

main = Tk()
ourMessage = "Jika kamu lihat ini berarti kamu ya sudalah"
messageVar = Message(main, text= ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
mainloop()