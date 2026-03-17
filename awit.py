import tkinter as tk 

window = tk.Tk()
window.title("PROFILE BUILDER")
window.geometry("600x500")
window.resizable(True, True)
window.configure(bg="black", cursor="arrow")

def sub():
    SID =tk.Toplevel()
    window.title("student ID")
    window.configure(bg="black")
    title = tk.Label(SID, text="Profile Builder", font=("arial", 20, "bold"), bg="black", fg="white")
    title.pack(pady=20)
    v = entry.get()
    entry.config(text=f"name {v}")
    entry.place(x= 20, y= 130)




    
def age():
    age1 = 2026
    age2 = entry3.get()
    sum = int(age1) - int(age2)
    C_btn.config(text=f"You are {sum} Years old")


#-----title-----
title = tk.Label(window, text="Profile Builder", font=("arial", 20, "bold"), bg="black", fg="white")
title.pack(pady=20)

F_name = tk.Label(window, text="First Name", font=("arial", 16, "bold"), fg="white", bg="black")
F_name.place(x= 20, y= 100)

entry = tk.Entry(window, width= 20, bg="black", fg="white")
entry.place(x= 20, y= 130)

M_name = tk.Label(window, text="Middle Name", font=("arial", 16, "bold"), fg="white", bg="black")
M_name.place(x= 220, y= 100)

entry1 = tk.Entry(window, width= 20, bg="black", fg="white")
entry1.place(x= 220, y= 130)

L_name = tk.Label(window, text="Last Name", font=("arial", 16, "bold"), fg="white", bg="black")
L_name.place(x= 420, y= 100)

entry2 = tk.Entry(window, width= 20, bg="black", fg="white")
entry2.place(x= 420, y= 130)

B_year = tk.Label(window, text="Birth Year", font=("arial", 16, "bold"), fg="white", bg="black")
B_year.place(x= 20, y= 200)

entry3 = tk.Entry(window, width= 20, bg="black", fg="white")
entry3.place(x= 20, y= 230)

gender = tk.Label(window, text="GENDER", font=("arial", 11,), fg="white", bg="black")
gender.place(x= 20, y= 280)

male = tk.Radiobutton(window, text="male", bg="white")
male.place(x= 220, y= 280)

female = tk.Radiobutton(window, text="female", bg="white")
female.place(x= 320, y= 280)

C_btn = tk.Button(window, text= "Clculate", bg="gray", fg="white", width= 20, command=age)
C_btn.place(x= 250, y= 200)

s_btn = tk.Button(window, text= "Submit", bg="gray", fg="white", width= 20, command=sub)
s_btn.place(x= 250, y= 400)







window.mainloop()