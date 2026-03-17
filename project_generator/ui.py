import tkinter as tk
from tkinter import messagebox
from project_generator.generator import generate_project


def create_project():
    name = entry_name.get()
    desc = entry_desc.get()
    author = entry_author.get()

    if not name:
        messagebox.showerror("Error", "Project name wajib diisi")
        return

    try:
        path = generate_project(name, desc, author)

        messagebox.showinfo(
            "Success",
            f"Project berhasil dibuat di:\n{path}"
        )

        # 🔥 Reset form setelah sukses
        entry_name.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# App
app = tk.Tk()
app.title("Project Generator")
app.geometry("400x300")
app.resizable(False, False)

# Container utama
frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Title
title = tk.Label(
    frame,
    text="Project Generator",
    font=("Arial", 14, "bold")
)
title.pack(pady=(0, 10))

# Project Name
tk.Label(frame, text="Project Name").pack(anchor="w")
entry_name = tk.Entry(frame)
entry_name.pack(fill="x", pady=5)

# Description
tk.Label(frame, text="Description").pack(anchor="w")
entry_desc = tk.Entry(frame)
entry_desc.pack(fill="x", pady=5)

# Author
tk.Label(frame, text="Author").pack(anchor="w")
entry_author = tk.Entry(frame)
entry_author.pack(fill="x", pady=5)
entry_author.insert(0, "FullstackDev")

# Button
generate_btn = tk.Button(
    frame,
    text="Generate Project",
    command=create_project,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=10,
    pady=8
)
generate_btn.pack(pady=15, fill="x")


def run():
    app.mainloop()