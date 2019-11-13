from tkinter import *

root = Tk()
turn = "X"
turnLabel = Label(root,text=turn,)
turnLabel.grid(row=3,columnspan=3)
ndex = 0
i = 0
x = 0
frame_list=[]
btn_list=[]
for i in range(3):
    for x in range(3):
        frame_list.append(Frame(root,width=200,height=200))
        frame_list[ndex].propagate(False)
        frame_list[ndex].grid(row= i, column = x,padx=10,pady=10)
        for y in range(3):
            btn_list.append(Button(frame_list[ndex],text="a"))
            btn_list[y].pack(expand=True,fill=BOTH)

        x+=1
        ndex+=1
    i+=1
root.resizable(width=False, height=False)
root.mainloop()
