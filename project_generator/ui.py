import tkinter as tk
from tkinter import messagebox
import os
from project_generator.generator import generate_project


# Simpan path terakhir
last_project_path = None


def open_folder():
    global last_project_path

    if last_project_path and os.path.exists(last_project_path):
        os.startfile(last_project_path)  # Windows
    else:
        messagebox.showerror("Error", "Belum ada project yang dibuat")


def create_project():
    global last_project_path

    name = entry_name.get()
    desc = entry_desc.get()
    author = entry_author.get()

    if not name:
        messagebox.showerror("Error", "Project name wajib diisi")
        return

    try:
        path = generate_project(name, desc, author)
        last_project_path = path

        messagebox.showinfo(
            "Success",
            f"Project berhasil dibuat di:\n{path}"
        )

        # 🔥 Auto buka folder
        os.startfile(path)

        # 🔥 Reset form
        entry_name.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# App
app = tk.Tk()
app.title("Project Generator")
app.geometry("400x350")
app.resizable(False, False)

# Container
frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Title
tk.Label(
    frame,
    text="Project Generator",
    font=("Arial", 14, "bold")
).pack(pady=(0, 10))

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

# Generate Button
tk.Button(
    frame,
    text="Generate Project",
    command=create_project,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    pady=8
).pack(pady=10, fill="x")

# 🔥 Open Folder Button
tk.Button(
    frame,
    text="Open Last Project Folder",
    command=open_folder,
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    pady=8
).pack(pady=5, fill="x")


def run():
    app.mainloop()