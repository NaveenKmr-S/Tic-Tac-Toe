from tkinter import * 
from tkinter import messagebox


root = Tk()
root.title("Tic-Tac-Toe")
root.resizable(0,0)

b_clicked= True
count=0

#diabling buttons
def disableButton():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    

#check winner
def check_win():
    global win
    if( b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
        b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
        b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
        b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
        b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
        b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
        b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        disableButton()
        messagebox.showinfo("Result", "X Wins")

    elif(count == 9):
        messagebox.showinfo("Result", "It is a Tie")

    elif(b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
        b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
        b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
        b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
        b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
        b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
        b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
        b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        disableButton()
        messagebox.showinfo("Result", "O Wins")


#button function
def buttonClick(bt):
    global b_clicked,count
    if bt["text"]=="" and b_clicked== True :
        bt["text"]="X"
        b_clicked=False
        count+=1
        check_win()
    elif bt["text"]=="" and b_clicked== False :
        bt["text"]="O"
        b_clicked=True
        count+=1
        check_win()
    else :
        messagebox.showerror(title="Error", message="Already Selected")

def reset():

    global b1,b2,b3,b4,b5,b6,b7,b8,b9,count,b_clicked
    count=0
    b_clicked=True
    #buttons
    b1 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b1))
    b2 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b2))
    b3 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b3))

    b4 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b4))
    b5 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b5))
    b6 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b6))

    b7 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b7))
    b8 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b8))
    b9 = Button(root,text="", height=5, width=10,font="Helvetica 20 bold", command= lambda: buttonClick(b9))

    #button placement
    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)

    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)

    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)

#menu 
menubar = Menu(root) 
root.config(menu=menubar) 
menubar.add_command(label="Reset", command=reset) 

reset()
root.mainloop()

