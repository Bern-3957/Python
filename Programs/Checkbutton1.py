import tkinter as tk

window = tk.Tk()
window.geometry("250x150+300+300")

#frm = tk.Frame(master=window, relief=tk.RAISED, bd=2)
#frm.grid(row=0, column=0)

checkb = tk.Checkbutton(master=window, text="Check please", fg="black", bg="blue")
checkb.place(x=80, y=50)


window.mainloop()