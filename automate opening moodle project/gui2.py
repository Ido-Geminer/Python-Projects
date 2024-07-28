import tkinter
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
def go_to_moodle(userinfo):
    if len(userinfo)!=3:
        tk.messagebox.showinfo("MISSING AN ENTRY ERROR", message="Fields Were Not Entered Correctly,\nTry FIlling Them Again")
        return None
    #load driver from its directory
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s=Service("C:\\Users\\ido geminer\\Desktop\\moodleprojcet\\chromedriver.exe")
    driver = webdriver.Chrome(options=options,service=s)
    driver.get("https://moodle.tau.ac.il/login/index.php")

    #elements i want to wait for and then i continue
    username=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,"Ecom_User_ID")))
    user_id=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,"Ecom_User_Pid")))
    password=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,"Ecom_Password")))

    #clear fields i want to use
    username.clear()
    user_id.clear()
    password.clear()

    #sending keys to fields
    username.send_keys(userinfo[0])
    user_id.send_keys(userinfo[1])
    password.send_keys(userinfo[2])

    #submiting fields and logging in
    submit=WebDriverWait(driver,7).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()

def collectinfo( username, id, password,userstorage):
    if not username.get() or not id.get() or not password.get():
        tk.messagebox.showinfo("INPUT ERROR", message="Invalid Input Was Entered, Try Again")
        return None
    else:
        userstorage.clear()
        userstorage.append(username.get())
        userstorage.append(id.get())
        userstorage.append(password.get())
        return None
#user info storing - [username,id,password]
userinformation=[]

# configuring gui
root = tk.Tk()
root.config(width=500, height=570)
root.title("TAU SHORTCUTS")
userinfo = []

# quit button
quit_button = tk.Button(root, text="QUIT", font="raleway", command=root.quit,borderwidth=2)
quit_button.config(height=2, width=5)
quit_button.place(x=220, y=500)

# moodle button
moodle_photo = tk.PhotoImage(file="moodlepic.png")
moodle_button = tk.Button(root, bg="white", image=moodle_photo, borderwidth=1,command=lambda:go_to_moodle(userinfo))
moodle_button.config(height=30, width=119)
moodle_button.place(x=100, y=33)

# store user inputs
username_input = tk.StringVar()
id_input = tk.StringVar()
password_input = tk.StringVar()

# username configure
username_label = tk.Label(root, text="Enter Username:")
username_label.place(x=100, y=280)
username = tk.Entry(root, textvariable=username_input)
username.place(x=100, y=300)
username.focus()

# id configure
id_label = tk.Label(root, text="Enter ID:")
id_label.place(x=100, y=320)
id = tk.Entry(root, textvariable=id_input)
id.place(x=100, y=340)
id.focus()

# user password
password_input_label = tk.Label(root, text="Enter Password:")
password_input_label.place(x=100, y=360)
password = tk.Entry(root, textvariable=password_input)
password.place(x=100, y=380)
password_input_label.focus()

#submit button configure
submit_button = tk.Button(root, text="Submit", borderwidth=1, command=lambda:collectinfo(username_input,id_input,password_input,userinfo))
submit_button.config(height=2, width=6)
submit_button.place(x=100, y=410)

root.mainloop()