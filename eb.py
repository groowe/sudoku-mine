import tkinter#, tkfont
import tkinter.font as font
top = tkinter.Tk()
right = tkinter.Frame(top)
right.pack(side = "right")
#font = tkFont.Font(family="Helvetica", size=20, weight = tkFont.BOLD)
myfont = font.Font(family='Helvetica')
for i in range(6):
    f = tkinter.Frame(right,width=100,height=100)
    b = tkinter.Button(f, text = str(i))#, font = font)
    b['font'] = myfont

    f.rowconfigure(0, weight = 1)
    f.columnconfigure(0, weight = 1)
    f.grid_propagate(0)

    f.grid(row = int(i/3), column = i%3)
    b.grid(sticky = "NWSE")

top.mainloop()
