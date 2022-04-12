import tkinter as tk

window = tk.Tk()

# def handle_keypress(event):
# 	print(event.char)

def cicl(ddd):
	print(f'Computer{ddd.char}')

window.bind("<Key>", cicl)

window.mainloop()