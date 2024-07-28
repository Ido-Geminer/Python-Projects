import tkinter as tk
import tkinter.messagebox as msg
Player1=[]
Player2=[]
P1_Wins=0
P2_Wins=0
#Making changes and X,0
def Pressed(event):
    print("SUCCESS")

    if P_Turn=="Player1":
        x=tk.PhotoImage(r"sC:\Users\DELL\Desktop\o.png")
        event["image"]=x
        #insert refrence to button to change picture
        Turn_Tracker+=1
    elif P_Turn=="Player2":
        o= tk.PhotoImage(r"C:\Users\DELL\Desktop\o.ppg")
        j=tk.Label(image=o,width=64,height=64)
        j.pack()
        Player2.append(2)
        Turn_Tracker+=1
    else:
        Invalid=tk.messagebox.showerror(title="ERROR",message="Your selection was already chosen try again")

#GUI settings
Main_Screen=tk.Tk()
Main_Screen.title("TIC TAC TOE")
Main_Screen.configure(bg="white")
bk_img=tk.PhotoImage(file=r"C:\Users\DELL\Desktop\R.png")
Backround_Label=tk.Label(Main_Screen,image=bk_img)
Backround_Label.place(x=0,y=0)
Main_Screen.geometry("415x400+450+150")
Main_Screen.resizable(False,False)
Main_Screen.option_add("dialog.msg.font","David 16")
Instruction_Lbl=tk.Label(Main_Screen,text="Instructions: The goal of tic-tac-toe is to be the \nfirst player to get three in a row on a 3-by-3 grid ",font=("David",16),bg="Blue")
Instruction_Lbl.pack()

#Buttons for game

# events
Playing=True
global Turn_Tracker
Turn_Tracker=0
while Playing==True:
    if Turn_Tracker % 2 == 0:
        P_Turn = "Player1"
    else:
        P_Turn = "Player2"
    But1 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4,command=lambda:Pressed(But1))

    But1.place(x=100, y=100)
   # But4 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
   # But4.bind("<Button-1>", Pressed(P_Turn,4))
   # But4.place(x=100, y=170)
  #  But7 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
  #  But7.place(x=100, y=240)
 #   But2 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
  #  But2.place(x=165, y=100)
  #  But5 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
  #  But5.place(x=165, y=170)
  #  But8 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
  #  But8.place(x=165, y=240)
   # But3 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
  #  But3.place(x=230, y=100)
 #   But6 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
   # But6.place(x=230, y=170)
   # But9 = tk.Button(Main_Screen, bg="white", borderwidth=2, width=8, height=4)
   # But9.place(x=230, y=240)
    Main_Screen.mainloop()