import tkinter as tk
import tkinter.messagebox as msgbx
import webbrowser
import maingen as RunMain
from PIL import ImageTk,Image
def click():
    Popup=msgbx.showinfo(title="Success!",message="Password - {0}".format(RunMain.main()))
def callback(URL):
    webbrowser.open_new(URL)
Main_Window=tk.Tk()
Main_Window.configure(bg="white")
Main_Window.geometry("600x680+300+10")
Main_Window.resizable(False,False)
Main_Window.title("Password Generator")
Main_Window.option_add("dialog.msg.font","David 16")
Instructions_Label=tk.Label(Main_Window,text="WELCOME! \n Click GENERATE to generate a password :) ",font=("David",18),bg="white")
Instructions_Label.pack()
Picture_Imp=Image.open("pswrdgenpic.jpeg")
Picture_Hldr=ImageTk.PhotoImage(Picture_Imp)
Picture_Label=tk.Label(Main_Window,image=Picture_Hldr,bg="white")
Picture_Label.pack()
Generating_Button=tk.Button(Main_Window,text="GENERATE PASSWORD",command=click,font=("David",18))
Generating_Button.pack()
Online_Check = tk.Label(Main_Window,
                        text="\nCheck the strength of the password here : " + "http://www.passwordmeter.com/",
                        font=("David,g8",10), fg="Blue",bg="white", cursor="hand2",)
Online_Check.bind("<Button-1>", lambda e: callback("http://www.passwordmeter.com/"))
Online_Check.pack()
Main_Window.mainloop()

