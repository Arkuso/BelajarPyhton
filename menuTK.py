from tkinter import *

root = Tk()
menu = Menu(root)

root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
helpmenu.add_command(label='3L')
helpmenu.add_separator()
helpmenu.add_command(label='Cingngok')

viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Tools window')
viewmenu.add_command(label='Appearance')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Definitiom')
viewmenu.add_command(label='Parameter Ingfo')
viewmenu.add_command(label='Type Ingfo')
viewmenu.add_command(label='Context Ingfo')
mainloop()
