import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
import threading
from project_generator.generator import generate_project

# ===== PATH =====
BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, "template")

last_project_path = None


# ===== TEMPLATE =====
def get_templates():
    return [
        name for name in os.listdir(TEMPLATE_DIR)
        if os.path.isdir(os.path.join(TEMPLATE_DIR, name))
    ]


def load_template_metadata(template_name):
    path = os.path.join(TEMPLATE_DIR, template_name, "template.json")

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    return {"description": "No description available"}


# ===== UI STATE =====
def update_status(text, color="#333"):
    status_label.config(text=text, fg=color)
    app.update_idletasks()


def set_loading(is_loading):
    if is_loading:
        generate_btn.config(state="disabled")
        open_btn.config(state="disabled")
        progress.start(10)
    else:
        generate_btn.config(state="normal")
        progress.stop()


# ===== ACTION =====
def open_folder():
    if last_project_path and os.path.exists(last_project_path):
        os.startfile(last_project_path)


def run_generation(name, desc, author, template):
    global last_project_path

    try:
        path = generate_project(name, desc, author, template)
        last_project_path = path

        update_status("Project created successfully 🎉", "green")

        open_btn.config(state="normal", bg="#2196F3")

        os.startfile(path)

        entry_name.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

    except Exception as e:
        update_status("Something went wrong ❌", "red")
        messagebox.showerror("Error", str(e))

    finally:
        set_loading(False)


def create_project():
    name = entry_name.get()
    desc = entry_desc.get()
    author = entry_author.get()
    template = template_var.get()

    if not name:
        update_status("Project name is required ⚠️", "red")
        messagebox.showerror("Error", "Project name wajib diisi")
        return

    update_status("Generating project... ⏳", "orange")
    set_loading(True)

    threading.Thread(
        target=run_generation,
        args=(name, desc, author, template),
        daemon=True
    ).start()


def on_template_change(event=None):
    selected = template_var.get()
    meta = load_template_metadata(selected)
    template_desc.config(text=meta["description"])


# ===== UI =====
app = tk.Tk()
app.title("Project Generator")
app.geometry("420x500")
app.resizable(False, False)

frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Title
tk.Label(
    frame,
    text="Project Generator",
    font=("Arial", 16, "bold")
).pack(pady=(0, 10))

# Inputs
tk.Label(frame, text="Project Name").pack(anchor="w")
entry_name = tk.Entry(frame)
entry_name.pack(fill="x", pady=5)

tk.Label(frame, text="Description").pack(anchor="w")
entry_desc = tk.Entry(frame)
entry_desc.pack(fill="x", pady=5)

tk.Label(frame, text="Author").pack(anchor="w")
entry_author = tk.Entry(frame)
entry_author.pack(fill="x", pady=5)
entry_author.insert(0, "Systemzerodev")

# Template Dropdown
tk.Label(frame, text="Template").pack(anchor="w")

template_var = tk.StringVar()
template_dropdown = ttk.Combobox(frame, textvariable=template_var, state="readonly")

templates = get_templates()
template_dropdown["values"] = templates

if templates:
    template_dropdown.current(0)

template_dropdown.pack(fill="x", pady=5)
template_dropdown.bind("<<ComboboxSelected>>", on_template_change)

# Template Description
template_desc = tk.Label(
    frame,
    fg="#666",
    wraplength=360,
    justify="left"
)
template_desc.pack(fill="x", pady=(5, 10))

on_template_change()

# Buttons
generate_btn = tk.Button(
    frame,
    text="Create Project",
    command=create_project,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    pady=10
)
generate_btn.pack(fill="x", pady=10)

open_btn = tk.Button(
    frame,
    text="Open Folder",
    command=open_folder,
    state="disabled",
    bg="#cccccc",
    fg="white",
    pady=10
)
open_btn.pack(fill="x")

# Progress Bar
progress = ttk.Progressbar(frame, mode="indeterminate")
progress.pack(fill="x", pady=10)

# Status
status_label = tk.Label(
    frame,
    text="Ready",
    anchor="w",
    fg="#333"
)
status_label.pack(fill="x")


def run():
    app.mainloop()