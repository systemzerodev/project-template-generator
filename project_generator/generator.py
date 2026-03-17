import os
import shutil
import importlib.util


# ================================
# PATH RESOLVER (AMAN DI SEMUA ENV)
# ================================
def get_base_dir():
    spec = importlib.util.find_spec("project_generator")
    if spec and spec.origin:
        return os.path.dirname(spec.origin)
    return os.path.dirname(__file__)


BASE_DIR = get_base_dir()
TEMPLATE_DIR = os.path.join(BASE_DIR, "template")
OUTPUT_DIR = "generated"


# ================================
# FILE YANG BOLEH DIPROSES
# ================================
ALLOWED_EXTENSIONS = {
    ".py", ".txt", ".md", ".json", ".rpy",
    ".html", ".js", ".css"
}


# ================================
# REPLACE PLACEHOLDER (SAFE)
# ================================
def replace_placeholders(file_path, data):
    _, ext = os.path.splitext(file_path)

    # skip file yang bukan text penting
    if ext.lower() not in ALLOWED_EXTENSIONS:
        return

    # baca file (toleransi error)
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except:
        return

    # replace placeholder
    for key, value in data.items():
        content = content.replace(f"{{{{{key.upper()}}}}}", value)

    # tulis ulang
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except:
        pass


# ================================
# MAIN GENERATOR
# ================================
def generate_project(project_name, description, author, template_name):
    # validasi template
    if not os.path.exists(TEMPLATE_DIR):
        raise Exception(f"Template directory tidak ditemukan:\n{TEMPLATE_DIR}")

    template_path = os.path.join(TEMPLATE_DIR, template_name)

    if not os.path.exists(template_path):
        available = os.listdir(TEMPLATE_DIR)
        raise Exception(
            f"Template '{template_name}' tidak ditemukan.\nAvailable: {available}"
        )

    # buat folder output
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, project_name)

    if os.path.exists(output_path):
        raise Exception(f"Project '{project_name}' sudah ada!")

    # copy template
    shutil.copytree(template_path, output_path)

    # data placeholder
    data = {
        "project_name": project_name,
        "description": description,
        "author": author,
    }

    # proses semua file
    for root, _, files in os.walk(output_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_placeholders(file_path, data)

    return output_path