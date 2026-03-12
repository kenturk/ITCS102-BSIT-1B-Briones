import tkinter as tk

window = tk.Tk()
window.title("SIMPLE CALCULATOR")
window.resizable(True, True)
window.configure(bg="black")
window.geometry("500x300")

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    label.config(text=f"The sum of {num1} + {num2} is {num1 + num2}")

def sub():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    label.config(text=f"The difference of {num1} - {num2} is {num1 - num2}")

def mlt():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    label.config(text=f"The product of {num1} × {num2} is {num1 * num2}")

def dvd():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    
    if num2 == 0:
        label.config(text="ERROR!!")
    else:
        label.config(text=f"The quotient of {num1} ÷ {num2} is {num1 / num2}")

label = tk.Label(window, text="SIMPLE CALCULATOR", font=("arial",20,"bold"), bg="black", fg="white")
label.grid(row=0, column=2, columnspan=2, pady=10)

label1 = tk.Label(window, text="Enter the First Number", font=("arial",15,"bold"), bg="black", fg="white")
label1.grid(row=1, column=0, columnspan=2, pady=10)

entry1 = tk.Entry(window, width=25, bg="black", fg="white")
entry1.grid(row=1, column=2, columnspan=2, pady=10)

label2 = tk.Label(window, text="Enter the Second Number", font=("arial",15,"bold"), bg="black", fg="white")
label2.grid(row=2, column=0, columnspan=2, pady=10)

entry2 = tk.Entry(window, width=25, bg="black", fg="white")
entry2.grid(row=2, column=2, columnspan=2, pady=10)

add_btn = tk.Button(window, text="ADDITION", bg="white", fg="black", width=15, command=add)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

sub_btn = tk.Button(window, text="SUBTRACTION", bg="white", fg="black", width=15, command=sub)
sub_btn.grid(row=5, column=1, columnspan=2, pady=10)

mlt_btn = tk.Button(window, text="MULTIPLICATION", bg="white", fg="black", width=15, command=mlt)
mlt_btn.grid(row=4, column=3, columnspan=2, pady=10)

dvd_btn = tk.Button(window, text="DIVISION", bg="white", fg="black", width=15, command=dvd)
dvd_btn.grid(row=5, column=3, columnspan=2, pady=10)

window.mainloop()