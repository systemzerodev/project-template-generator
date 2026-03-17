import os
import json
import threading
import ctypes
import importlib.util
import tkinter as tk
from tkinter import ttk, messagebox

from project_generator.generator import generate_project

# ===== FIX TASKBAR ICON =====
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("project.generator.app")


# ===== PATH RESOLVER =====
def get_base_dir():
    spec = importlib.util.find_spec("project_generator")
    if spec and spec.origin:
        return os.path.dirname(spec.origin)
    return os.path.dirname(__file__)

BASE_DIR = get_base_dir()
TEMPLATE_DIR = os.path.join(BASE_DIR, "template")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

last_project_path = None


# ===== TEMPLATE =====
def get_templates():
    if not os.path.exists(TEMPLATE_DIR):
        return []
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


def set_loading(state):
    if state:
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

        update_status("Project created 🎉", "green")
        open_btn.config(state="normal")

        os.startfile(path)

        entry_name.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

    except Exception as e:
        update_status("Error ❌", "red")
        messagebox.showerror("Error", str(e))

    finally:
        set_loading(False)


def create_project():
    name = entry_name.get()
    desc = entry_desc.get()
    author = entry_author.get()
    template = template_var.get()

    if not name:
        messagebox.showerror("Error", "Project name wajib diisi")
        return

    update_status("Generating... ⏳", "orange")
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


# ===== UI INIT =====
app = tk.Tk()
app.title("Project Generator")
app.geometry("420x500")
app.resizable(False, False)

# ICON
icon_path = os.path.join(ASSETS_DIR, "icon.ico")
if os.path.exists(icon_path):
    try:
        app.iconbitmap(icon_path)
    except:
        pass


# ===== LAYOUT =====
frame = tk.Frame(app, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Project Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(frame, text="Project Name").pack(anchor="w")
entry_name = tk.Entry(frame)
entry_name.pack(fill="x", pady=5)

tk.Label(frame, text="Description").pack(anchor="w")
entry_desc = tk.Entry(frame)
entry_desc.pack(fill="x", pady=5)

tk.Label(frame, text="Author").pack(anchor="w")
entry_author = tk.Entry(frame)
entry_author.insert(0, "Systemzerodev")
entry_author.pack(fill="x", pady=5)

# TEMPLATE
tk.Label(frame, text="Template").pack(anchor="w")

template_var = tk.StringVar()
template_dropdown = ttk.Combobox(frame, textvariable=template_var, state="readonly")

templates = get_templates()
template_dropdown["values"] = templates

if templates:
    template_dropdown.current(0)

template_dropdown.pack(fill="x", pady=5)
template_dropdown.bind("<<ComboboxSelected>>", on_template_change)

template_desc = tk.Label(frame, fg="#666", wraplength=360, justify="left")
template_desc.pack(fill="x", pady=5)

on_template_change()

# BUTTONS
generate_btn = tk.Button(frame, text="Create Project", command=create_project, bg="#4CAF50", fg="white")
generate_btn.pack(fill="x", pady=10)

open_btn = tk.Button(frame, text="Open Folder", command=open_folder, state="disabled")
open_btn.pack(fill="x")

# PROGRESS
progress = ttk.Progressbar(frame, mode="indeterminate")
progress.pack(fill="x", pady=10)

# STATUS
status_label = tk.Label(frame, text="Ready", anchor="w")
status_label.pack(fill="x")


def run():
    app.mainloop()