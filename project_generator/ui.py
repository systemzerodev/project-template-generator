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
        messagebox.showinfo("Success", f"Project dibuat di:\n{path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


app = tk.Tk()
app.title("Project Generator")
app.geometry("400x250")

tk.Label(app, text="Project Name").pack(pady=5)
entry_name = tk.Entry(app)
entry_name.pack(pady=5)

tk.Label(app, text="Description").pack(pady=5)
entry_desc = tk.Entry(app)
entry_desc.pack(pady=5)

tk.Label(app, text="Author").pack(pady=5)
entry_author = tk.Entry(app)
entry_author.pack(pady=5)

entry_author.insert(0, "Systemzerodev")

tk.Button(app, text="Generate", command=create_project).pack(pady=10)


def run():
    app.mainloop()