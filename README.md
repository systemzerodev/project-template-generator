# 🚀 Project Template Generator

Tool berbasis Python untuk membuat project baru secara otomatis menggunakan template.

Cukup jalankan satu command → isi form → project langsung siap digunakan.

---

## ✨ Features

- ⚡ Generate project hanya dengan satu klik
- 🧱 Struktur project otomatis
- 🔁 Replace placeholder (`{{PROJECT_NAME}}`, dll)
- 🖥️ UI sederhana (Tkinter)
- 💻 CLI command: `create-project`
- 📦 Bisa di-install dan digunakan di mana saja

---

## 📦 Installation

### 🔹 Install dari GitHub

```bash
pip install git+https://github.com/USERNAME/project-template-generator.git
```

---

## 🚀 Usage

Jalankan command:

```bash
create-project
```

Akan muncul UI:

- Isi **Project Name**
- Isi **Description**
- Isi **Author**
- Klik **Generate**

Project akan otomatis dibuat di folder:

```bash
generated/
```

---

## 📁 Example Output

```bash
generated/
└── my_project/
    ├── README.md
    ├── main.py
    └── config/
        └── config.json
```

---

## 🧠 How It Works

1. Template diambil dari folder `template/`
2. Semua placeholder diganti sesuai input user
3. Project baru dibuat secara otomatis

---

## 🛠️ Tech Stack

- Python
- Tkinter (UI)
- setuptools (CLI & packaging)

---

## 📌 Project Structure

```bash
project-template-generator/
│
├── project_generator/
│   ├── generator.py
│   ├── ui.py
│   └── __init__.py
│
├── template/
│   ├── README.md
│   ├── main.py
│   └── config/
│       └── config.json
│
├── setup.py
├── MANIFEST.in
├── README.md
└── LICENSE
```

---

## 🔧 Development Setup

```bash
git clone https://github.com/systemzerodev/project-template-generator.git
cd project-template-generator

python -m venv .venv
.venv\Scripts\activate

pip install .
```

---

## 🔮 Roadmap

- [ ] Multi-template support (web, flutter, dll)
- [ ] CLI mode tanpa UI
- [ ] Auto open project di VS Code
- [ ] Export ke .exe

---

## 📄 License

MIT License

---

## 👤 Author

Systemzerodev

---

## ⭐ Notes

Project ini dibuat untuk:

- mempercepat workflow development
- latihan membuat developer tools dari nol
