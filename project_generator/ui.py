import tkinter as tk
from tkinter import messagebox, ttk
import os
import threading
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


def run_generation(name, desc, author):
    global last_project_path

    try:
        path = generate_project(name, desc, author)
        last_project_path = path

        # Stop loading
        progress.stop()

        update_status("Project created successfully!", "green")

        # Aktifkan tombol
        open_btn.config(state="normal", bg="#2196F3")

        # Auto buka folder
        os.startfile(path)

        # Reset form
        entry_name.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

    except Exception as e:
        progress.stop()
        update_status("Error occurred", "red")
        messagebox.showerror("Error", str(e))


def create_project():
    name = entry_name.get()
    desc = entry_desc.get()
    author = entry_author.get()

    if not name:
        update_status("Project name wajib diisi", "red")
        messagebox.showerror("Error", "Project name wajib diisi")
        return

    # 🔥 Start loading animation
    update_status("Generating project...", "orange")
    progress.start(10)

    # 🔥 Run di thread
    threading.Thread(
        target=run_generation,
        args=(name, desc, author),
        daemon=True
    ).start()


# App
app = tk.Tk()
app.title("Project Generator")
app.geometry("400x420")
app.resizable(False, False)

frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Title
tk.Label(
    frame,
    text="Project Generator",
    font=("Arial", 14, "bold")
).pack(pady=(0, 10))

# Input
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

# Open Folder Button
open_btn = tk.Button(
    frame,
    text="Open Last Project Folder",
    command=open_folder,
    bg="#cccccc",
    fg="white",
    state="disabled",
    pady=8
)
open_btn.pack(pady=5, fill="x")

# 🔥 PROGRESS BAR
progress = ttk.Progressbar(
    frame,
    mode="indeterminate"
)
progress.pack(fill="x", pady=10)

# Status
status_label = tk.Label(
    frame,
    text="Ready",
    fg="#333",
    anchor="w"
)
status_label.pack(fill="x")


def run():
    app.mainloop()