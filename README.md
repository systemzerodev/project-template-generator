# 🚀 Project Template Generator

Tool sederhana berbasis Python untuk membuat project baru secara otomatis menggunakan template.

Dengan tool ini, kamu bisa membuat project hanya dengan satu command dan UI tanpa perlu setup manual.

---

## ✨ Features

- 🧱 Generate struktur project otomatis
- 🔁 Replace placeholder (`{{PROJECT_NAME}}`, dll)
- 🖥️ UI berbasis Tkinter (mudah digunakan)
- ⚡ CLI command: `create-project`
- 📦 Bisa di-install seperti tool profesional

---

## 📁 Project Structure

```
project-template-generator/
│
├── project_generator/
│   ├── generator.py
│   ├── ui.py
│   └── __init__.py
│
├── template/
│   ├── README.md
│   └── main.py
│
├── setup.py
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

Clone repository:

```
git clone https://github.com/systemzerodev/project-template-generator.git
cd project-template-generator
```

Aktifkan virtual environment (opsional tapi disarankan):

```
python -m venv .venv
.venv\Scripts\activate
```

Install tool:

```
pip install .
```

---

## 🚀 Usage

Jalankan command:

```
create-project
```

Akan muncul UI:

- Isi nama project
- Isi deskripsi
- Isi author
- Klik **Generate**

Project akan otomatis dibuat di folder `generated/`

---

## 📌 Example Output

```
generated/
└── my_project/
    ├── README.md
    └── main.py
```

---

## 🧠 How It Works

1. Template disalin dari folder `template/`
2. Placeholder diganti dengan input user
3. Project baru dibuat di folder `generated/`

---

## 🛠️ Tech Stack

- Python
- Tkinter (UI)
- setuptools (packaging)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🔥 Future Improvements

- Multi-template support (web, flutter, dll)
- CLI tanpa UI (interactive terminal)
- Auto open project di VS Code
- Packaging ke `.exe`

---

## 🤝 Contributing

Feel free to fork dan kembangkan sesuai kebutuhan.

---

## 💡 Author

**FullstackDev**

---

## ⭐ Notes

Tool ini dibuat untuk mempercepat workflow development dan sebagai latihan membangun developer tooling dari nol.
