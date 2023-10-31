from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)
redbutton = Button(frame,text='RED', fg='RED')
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text='Green', fg='green')
greenbutton.pack(side=LEFT)
brownbutton = Button(frame, text='Brown', fg='brown')
brownbutton.pack(side=LEFT)                 

mainloop()