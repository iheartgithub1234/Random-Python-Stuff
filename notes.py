import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def save_note():
    note_text = text.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(note_text)
        messagebox.showinfo("Note Saved", "Note has been saved successfully.")

def open_note():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            note_text = file.read()
            text.delete("1.0", "end")
            text.insert("1.0", note_text)

def clear_note():
    text.delete("1.0", "end")

# Create the main application window
root = tk.Tk()
root.title("Notes App")
root.geometry("400x300")

# Create the text widget
text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

# Create the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Note", command=clear_note)
file_menu.add_command(label="Open Note", command=open_note)
file_menu.add_command(label="Save Note", command=save_note)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run the application
root.mainloop()