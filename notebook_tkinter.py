import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Notepad")

def exit_app():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")

# Создание текстовой области и прокрутки
text_area = tk.Text(root, wrap=tk.WORD)
scrollbar = tk.Scrollbar(root, command=text_area.yview)
text_area.configure(yscrollcommand=scrollbar.set)

# Расположение виджетов
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.pack(expand=True, fill=tk.BOTH)

# Создание меню
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()
