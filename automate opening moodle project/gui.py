import tkinter
import tkinter as tk
from tkinter import *
#configuring gui
root= tk.Tk()


class GUI:

    def __init__(self,master_win):
        #window configure
        self.master_win=master_win
        master_win.config(width=500,height=570)
        master_win.title("TAU SHORTCUTS")
        self.userinfo=[]
        #quit button
        self.quit_button= tk.Button(self.master_win,text="QUIT",font="raleway",command=master_win.quit, borderwidth=2)
        self.quit_button.config(height=2,width=5)
        self.quit_button.place(x=220, y=500)

        #moodle button
        self.moodle_photo=tk.PhotoImage(file="moodlepic.png")
        self.moodle_button=tk.Button(self.master_win,bg="white", image=self.moodle_photo,borderwidth=1)
        self.moodle_button.config(height=30,width=119)
        self.moodle_button.place(x=100,y=33)

        # store user inputs
        self.username_input=tk.StringVar()
        self.id_input=tk.StringVar()
        self.password_input=tk.StringVar()

        #username configure
        self.username_label=tk.Label(self.master_win,text="Enter Username:")
        self.username_label.place(x=100,y=280)
        self.username=tk.Entry(self.master_win,textvariable=self.username_input)
        self.username.place(x=100,y=300)
        self.username.focus()

        #id configure
        self.id_label = tk.Label(self.master_win, text="Enter ID:")
        self.id_label.place(x=100, y=320)
        self.id = tk.Entry(self.master_win, textvariable=self.id_input)
        self.id.place(x=100, y=340)
        self.id.focus()

        #user password
        self.password_input_label = tk.Label(self.master_win, text="Enter Password:")
        self.password_input_label.place(x=100, y=360)
        self.password = tk.Entry(self.master_win, textvariable=self.password_input)
        self.password.place(x=100, y=380)
        self.password_input_label.focus()

        self.submit_info = tk.Button(self.master_win, text="Submit", borderwidth=1,command=GUI.get_info())
        self.submit_info.config(height=2, width=6)
        self.submit_info.place(x=100, y=410)

    
class Userinfo(GUI):
    def __init__(self,master_win):
        GUI.__init__(self,master_win)
        self.master_win=master_win
        self.submit_info = tk.Button(self.master_win, text="Submit", borderwidth=1)
        self.submit_info.config(height=2, width=6)
        self.submit_info.place(x=100, y=410)

    def collectinfo(self,username,id,password):
        self.userinfo.clear()
        self.userinfo.append(username.get())
        self.userinfo.append(id.get())
        self.userinfo.append(password.get())
        print(self.userinfo)

x=GUI(root)
root.mainloop()