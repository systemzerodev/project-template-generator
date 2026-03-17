import tkinter as tk
from tkinter import messagebox
import os
from project_generator.generator import generate_project


last_project_path = None


def update_status(text, color="#333"):
    status_label.config(text=text, fg=color)
    app.update_idletasks()


def open_folder():
    global last_project_path

    if last_project_path and os.path.exists(last_project_path):
        os.startfile(last_project_path)
    else:
        messagebox.showerror("Error", "Belum ada project yang dibuat")


def create_project():
    global last_project_path

    name = entry_name.get()
    desc = entry_desc.get()
    author = entry_author.get()

    if not name:
        update_status("Project name wajib diisi", "red")
        messagebox.showerror("Error", "Project name wajib diisi")
        return

    try:
        update_status("Generating project...", "orange")

        path = generate_project(name, desc, author)
        last_project_path = path

        update_status("Project created successfully!", "green")

        messagebox.showinfo(
            "Success",
            f"Project berhasil dibuat di:\n{path}"
        )

        # Auto buka folder
        os.startfile(path)

        # Reset form
        entry_name.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

        # Aktifkan tombol open folder
        open_btn.config(state="normal", bg="#2196F3")

    except Exception as e:
        update_status("Error occurred", "red")
        messagebox.showerror("Error", str(e))


# App
app = tk.Tk()
app.title("Project Generator")
app.geometry("400x380")
app.resizable(False, False)

frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Title
tk.Label(
    frame,
    text="Project Generator",
    font=("Arial", 14, "bold")
).pack(pady=(0, 10))

# Input fields
tk.Label(frame, text="Project Name").pack(anchor="w")
entry_name = tk.Entry(frame)
entry_name.pack(fill="x", pady=5)

tk.Label(frame, text="Description").pack(anchor="w")
entry_desc = tk.Entry(frame)
entry_desc.pack(fill="x", pady=5)

tk.Label(frame, text="Author").pack(anchor="w")
entry_author = tk.Entry(frame)
entry_author.pack(fill="x", pady=5)
entry_author.insert(0, "FullstackDev")

# Generate button
tk.Button(
    frame,
    text="Generate Project",
    command=create_project,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    pady=8
).pack(pady=10, fill="x")

# Open folder button
open_btn = tk.Button(
    frame,
    text="Open Last Project Folder",
    command=open_folder,
    bg="#cccccc",
    fg="white",
    activebackground="#1976D2",
    pady=8,
    state="disabled"
)
open_btn.pack(pady=5, fill="x")

# 🔥 STATUS LABEL (INI YANG BARU)
status_label = tk.Label(
    frame,
    text="Ready",
    fg="#333",
    anchor="w"
)
status_label.pack(fill="x", pady=(10, 0))


def run():
    app.mainloop()