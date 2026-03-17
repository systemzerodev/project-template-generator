🚀 Project Template Generator

Generate project in seconds with a simple command.

---

⚡ Quick Start

1. Install pipx (one-time setup)

pip install pipx
pipx ensurepath

«⚠️ Restart your terminal after running "pipx ensurepath"»

---

2. Install Project Generator

pipx install git+https://github.com/systemzerodev/project-template-generator.git

---

3. Run the Tool

create-project

---

🧠 How It Works

- pipx creates an isolated environment automatically
- No need to manage virtual environments
- Command is available globally after install

---

📦 What Happens Next?

After running "create-project":

- A simple UI will appear
- Fill in your project details
- Your project will be generated instantly

---

📁 Output Example

generated/
└── my_project/
├── README.md
├── main.py
└── config/
└── config.json

---

🔧 Alternative (Manual Setup)

python -m venv .venv
.venv\Scripts\activate

pip install git+https://github.com/systemzerodev/project-template-generator.git

create-project

---

📌 Requirements

- Python 3.8+

---

👨‍💻 Author

Systemzerodev
