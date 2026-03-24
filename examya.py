import tkinter as tk

window = tk.Tk()
window.title(" LOGIN")
window.resizable(True, True)
window.configure(bg="black",cursor="cross")
window.geometry("1000x350")


def RT():
    RT =tk.Toplevel()
    RT.title("REGITRATION FORM")
    RT.configure(bg="black")
    RT.geometry("500x150")

    title = tk.Label(RT, text="REGITRATION FORM", font=("arial", 20, "bold"), bg="black", fg="white")
    title.grid(row= 1, column= 1, columnspan= 3)

    label = tk.Label(RT, text="Username", font=("arial", 15,), bg="black", fg="white")
    label.grid(row= 2, column= 1, columnspan= 3)

    entry = tk.Entry(RT, width= 25, bg="black", fg="white")
    entry.grid(row= 2, column= 4, columnspan= 3)

    label1 = tk.Label(RT, text="Password", font=("arial", 15,), bg="black", fg="white")
    label1.grid(row= 3, column= 1, columnspan= 3)

    entry1 = tk.Entry(RT, width= 25, bg="black", fg="white", show="*")
    entry1.grid(row= 3, column= 4, columnspan= 3)

    spass = tk.Checkbutton(RT, text="Show Password", bg="black", fg="purple")
    spass.grid(row= 4, column= 3, columnspan= 3)
    
    rt1_btn = tk.Button(RT, text= "register",font=("arial", 10, "bold"), bg="black", fg="white", width=15, height=1)
    rt1_btn.grid(row= 5, column= 3, columnspan= 3)

def lgn():
    lgn = tk.Toplevel()
    lgn.title("LOG IN")
    lgn.configure(bg="black")
    lgn.geometry("300x150")
    
    title = tk.Label(lgn, text="LOG IN", font=("arial", 20, "bold"), bg="black", fg="white")
    title.grid(row= 0, column= 1, columnspan= 3)

    label = tk.Label(lgn, text="Username", font=("arial", 15,), bg="black", fg="white")
    label.grid(row= 1, column= 1, columnspan= 3)

    entry = tk.Entry(lgn, width= 25, bg="black", fg="white")
    entry.grid(row= 1, column= 4, columnspan= 3)

    label1 = tk.Label(lgn, text="Password", font=("arial", 15,), bg="black", fg="white")
    label1.grid(row= 2, column= 1, columnspan= 3)

    entry1 = tk.Entry(lgn, width= 25, bg="black", fg="white", show="*")
    entry1.grid(row= 2, column= 4, columnspan= 3)

    spass = tk.Checkbutton(lgn, text="Show Password", bg="black", fg="white",)
    spass.grid(row= 3, column= 3, columnspan= 3)
    rt1_btn = tk.Button(lgn, text= "register",font=("arial", 10, "bold"), bg="black", fg="white", width=15, height=1)
    rt1_btn.grid(row= 4, column= 3, columnspan= 3)

label1 = tk.Label(window, text="WELCOME", font=("arial", 10, "bold"), fg="black", bg="white")
label1.grid(row= 0, column= 1, columnspan= 3, pady= 10)


rt_btn = tk.Button(window, text= "REGISTER",font=("arial", 10, "bold"), bg="black", fg="white", width=130, height=5, command=RT)
rt_btn.grid(row= 1, column= 1, columnspan= 3, pady= 10)

lgn_btn = tk.Button(window, text= "LOG IN",font=("arial", 10, "bold"), bg="black", fg="white", width=130, height=5, command=lgn)
lgn_btn.grid(row= 2, column= 3, columnspan= 3, pady= 10)

window.mainloop()