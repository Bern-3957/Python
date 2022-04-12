import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename, asksaveasfile, Scrollbar, LEFT, Y, Frame

FILE_NAME = tk.NONE
 
def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r", filetypes=[("Текстовые фйлы", "*.txt"), ("Все файлы", "*.*")])
    if inp is None:
        return
    FILE_NAME = inp.name
    print(FILE_NAME)
 
    data = inp.read()
    txt_edit.delete('1.0', tk.END)
    txt_edit.insert("1.0", FILE_NAME+"\n")
    txt_edit.insert(tk.END, data)
 
def save_file():
    
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые фйлы", "*.txt"), ("Все файлы", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Простой текстовый редактор - {filepath}")
 
def also_save():
    data = txt_edit.get('1.0', tk.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()
def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    txt_edit.delete("0.0", tk.END)
    txt_edit.insert("0.0", FILE_NAME)


window = tk.Tk()
window.title("Простой текстовый редактор")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
 
txt_edit = tk.Text(window)

scroll_frm = Frame()
scroll = Scrollbar(scroll_frm, command=txt_edit.yview)
scroll.pack(side=LEFT, fill=Y)
txt_edit.config(yscrollcommand=scroll.set)
scroll_frm.grid(rowspan=5, column=2)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)
btn_save_as = tk.Button(fr_buttons, text="Сохранить как...", command=save_file)
btn_also_save = tk.Button(fr_buttons, text="Сохранить", command=also_save)
btn_new = tk.Button(fr_buttons, text="Новый файл", command=new_file)
 
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save_as.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_also_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_new.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
 
window.mainloop()