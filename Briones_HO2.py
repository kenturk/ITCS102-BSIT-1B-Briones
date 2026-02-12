import tkinter as tk
window = tk.Tk()

window.title("BRIONES_HO2")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="black")

label = tk.Label(window, text="STUDENT PROFILE", font=("Arial", 14, "bold"), bg="black",fg="white")
label.pack(pady=20)

label = tk.Label(window, text="Full Name: Ken Wesley V. Briones", font=("Arial", 14), bg="black",fg="white")
label.pack(pady=20, padx=20,anchor="w")

label = tk.Label(window, text="Age: 19years old", font=("Arial", 14), bg="black",fg="white", justify= "left")
label.pack(pady=20, padx=20,anchor="w")

label = tk.Label(window, text="Course: BSIT - 1B", font=("Arial", 14), bg="black",fg="white", justify= "left")
label.pack(pady=20, padx=20, anchor="w")

label = tk.Label(window, text="Birthday: August 15, 2006", font=("Arial", 14), bg="black",fg="white", justify= "left")
label.pack(pady=20,padx=20, anchor="w")

label = tk.Label(window, text="Motto:", font=("Arial", 14), bg="black",fg="white", justify= "left")
label.pack(pady=20, padx=20, anchor="w")

label = tk.Label(window, text=f"""         Be a Better Person Than You Are Yesterday and 
Help Others, It Doesn't Have To Be Everyday As 
Long As You Help Someone Even If It's The Bare Minimum. 
Help Someone If You Can """, font=("Arial", 14), bg="black",fg="white", justify= "left")
label.pack(anchor="center")
window.mainloop()