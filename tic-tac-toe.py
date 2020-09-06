from tkinter import *

def callback(r,c):
    global player

    if player=='X' and some[r][c]==0 and stop_game==False:
        b[r][c].configure(text='X', fg="green",bg="white")
        some[r][c]='X'
        player='O'

    if player=='O' and some[r][c]==0 and stop_game==False:
        b[r][c].configure(text='O', fg="orange",bg="black")
        some[r][c]='O'
        player='X' 
    check_winner()

def check_winner():
    global stop_game
    for i in range(3):
        if some[i][0]==some[i][1]==some[i][2]!=0:
            b[i][0].configure(bg='yellow')
            b[i][1].configure(bg='yellow')
            b[i][2].configure(bg='yellow')
            stop_game=True
    for i in range(3):
        if some[0][i]==some[1][i]==some[2][i]!=0:
            b[0][i].configure(bg='yellow')
            b[1][i].configure(bg='yellow')
            b[2][i].configure(bg='yellow')
            stop_game=True 
    if some[0][0]==some[1][1]==some[2][2]!=0: 
        b[0][0].configure(bg='yellow')
        b[1][1].configure(bg='yellow')
        b[2][2].configure(bg='yellow')
        stop_game=True  
    if some[2][0]==some[1][1]==some[0][2]!=0:
        b[2][0].configure(bg='yellow')
        b[1][1].configure(bg='yellow')
        b[0][2].configure(bg='yellow')
        stop_game=True                              
   




root=Tk()
root.title("Tic Tac Toe *lol")
b=[[0,0,0],
   [0,0,0],
   [0,0,0]]
some=[[0,0,0],
      [0,0,0],
      [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(font=("bubble",60),width=4,bg='light blue',command= lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)   
player='X'
stop_game=False

mainloop()
