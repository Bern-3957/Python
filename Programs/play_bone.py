import tkinter as tk
from random import randint

def make():
	#value = frame_label["text"]
	value = randint(1, 6)
	frame_label["text"] = f"{value}"

window = tk.Tk()

frame = tk.Frame()
frame.pack()

frame_btn = tk.Button(master=frame, text="Бросить", command=make, padx=5, pady=5)
frame_btn.grid(row=0, column=0, sticky="ew")

frame_label = tk.Label(master=frame, text=0)
frame_label.grid(row=1, column=0)




window.mainloop()