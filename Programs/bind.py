import tkinter as tk

window = tk.Tk()
def handle_click(event):
	print("The button is clicked!")

button = tk.Button(text="Click please")
button.pack()
button.bind("<Button-1>", handle_click)	

window.mainloop()