import tkinter as tk
import tkinter.messagebox as msg
from PIL import Image,ImageTk
global Player1
Player1=[]
global Player2
Player2=[]
global P1_Wins
P1_Wins=0
global P2_Wins
P2_Wins=0

#GUI settings
Main_Screen=tk.Tk()
Main_Screen.title("TIC TAC TOE")
Main_Screen.configure(bg="white")
bg_img_holder=Image.open("bgpic2.jpeg")
bk_img=ImageTk.PhotoImage(bg_img_holder)
Backround_Label=tk.Label(Main_Screen,image=bk_img)
Backround_Label.place(x=-4,y=-17)
Main_Screen.geometry("415x400+450+150")
Main_Screen.resizable(False,False)
Main_Screen.option_add("dialog.msg.font","David 16")

#XO Function
def Pressed1(event,num):
    global Turn_Tracker

    if Turn_Tracker % 2 == 0:
      #  x=tk.PhotoImage(r"C:\Users\DELL\Desktop\x.png")
        event["text"]="x"
        event.configure(anchor="center")
     #   event.configure(width=64,height=64)
        Player1.append(num)
        event.configure(state="disabled")
        print("K")
        print(Player1)
        Turn_Tracker+=1
        Win_Check(Player1, Player2)
        return Turn_Tracker
    if Turn_Tracker % 2 != 0:
      #  x=tk.PhotoImage(r"C:\Users\DELL\Desktop\x.png")
        event["text"]="o"
        event.configure(anchor="center")
     #   event.configure(width=64,height=64)
        Player2.append(num)
        event.configure(state="disabled")
        print("Kk")
        print(Player2)
        Turn_Tracker += 1
        Win_Check(Player1,Player2)
        return Turn_Tracker
#reset board Buttons Functions
def reset(num):
    global Player1,P1_Wins,Player2,P2_Wins,Turn_Tracker
    Player1=[]
    global Player2
    Player2=[]
    if num==1:
        P1_Wins+=1
    if num==2:
        P2_Wins+=1
    if num==3:
        pass
    Turn_Tracker=0
    But1.configure(state="normal",text="")
    But2.configure(state="normal", text="")
    But3.configure(state="normal", text="")
    But4.configure(state="normal", text="")
    But5.configure(state="normal", text="")
    But6.configure(state="normal", text="")
    But7.configure(state="normal", text="")
    But8.configure(state="normal", text="")
    But9.configure(state="normal", text="")
    Score_Label.configure(text="Player 1- {0} Player 2 - {1}".format(P1_Wins, P2_Wins))
    return Player1,Player2,P2_Wins,P1_Wins
#checking Winning function
def Win_Check(Player1,Player2):
    #check player 1 wins
    if 1 in Player1 and 2 in Player1 and 3 in Player1 :
        Win_Label=msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
          pass
    if 4 in Player1 and 5 in Player1 and 6 in Player1:
        Win_Label = msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
            pass
    if 7 in Player1 and 8 in Player1 and 9 in Player1:
        Win_Label = msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
            pass
    if 1 in Player1 and 4 in Player1 and 7 in Player1:
        Win_Label = msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
            pass
    if 2 in Player1 and 5 in Player1 and 8 in Player1:
        Win_Label = msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
            pass
    if 3 in Player1 and 6 in Player1 and 9 in Player1:
        Win_Label = msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
            pass
    if 1 in Player1 and 5 in Player1 and 9 in Player1:
        Win_Label = msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
            pass
    if 3 in Player1 and 5 in Player1 and 7 in Player1:
        Win_Label = msg.askyesno(message="Player 1 Won! \nWould you like to Play again?")
        if "yes":
            reset(1)
        if "no":
            pass
   #Player 2 win options
    if 1 in Player2 and 2 in Player2 and 3 in Player2 :
        Win_Label=msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if 4 in Player2 and 5 in Player2 and 6 in Player2:
        Win_Label = msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if 7 in Player2 and 8 in Player2 and 9 in Player2:
        Win_Label = msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if 1 in Player2 and 4 in Player2 and 7 in Player2:
        Win_Label = msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if 2 in Player2 and 5 in Player2 and 8 in Player2:
        Win_Label = msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if 3 in Player2 and 6 in Player2 and 9 in Player2:
        Win_Label = msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if 1 in Player2 and 5 in Player2 and 9 in Player2:
        Win_Label = msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if 3 in Player2 and 5 in Player2 and 7 in Player2:
        Win_Label = msg.askyesno(message="Player 2 Won! \nWould you like to Play again?")
        if "yes":
            reset(2)
        if "no":
            pass
    if (len(Player1)==4 and len(Player2)==5) or (len(Player1)==5 and len(Player2)==4):
        Tie_Label=msg.askyesno(message="Tie! \nWould you like to Play again?")
        if "yes":
            reset(3)
        if "no":
            pass
Playing=True
Turn_Tracker=0
Score_Label=tk.Label(Main_Screen,text="Player 1- {0} Player 2 - {1}".format(P1_Wins,P2_Wins),font=("David",20),anchor="center")
Score_Label.place(x=80,y=40)
Quit_Button=tk.Button(Main_Screen,text="Quit",command=Main_Screen.destroy)
Quit_Button.place(x=300,y=300)
while Playing==True:
    print(Player1)
    print("____________")
    print(Player2)
    print(P1_Wins)
    print(P2_Wins)
    But1 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda:Pressed1(But1, 1))
    But1.place(x=100, y=100)
    But4 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But4, 4))
    But4.place(x=100, y=170)
    But7 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But7, 7))
    But7.place(x=100, y=240)
    But2 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But2, 2))
    But2.place(x=165, y=100)
    But5 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But5, 5))
    But5.place(x=165, y=170)
    But8 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But8, 8))
    But8.place(x=165, y=240)
    But3 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But3, 3))
    But3.place(x=230, y=100)
    But6 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But6, 6))
    But6.place(x=230, y=170)
    But9 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,
                     command=lambda: Pressed1(But9, 9))
    But9.place(x=230, y=240)

    Win_Check(Player1,Player2)
    Main_Screen.mainloop()