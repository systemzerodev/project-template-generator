import os
import shutil
import importlib.util

# ===== PATH RESOLVER (ANTI ERROR) =====
def get_base_dir():
    spec = importlib.util.find_spec("project_generator")
    if spec and spec.origin:
        return os.path.dirname(spec.origin)
    return os.path.dirname(__file__)

BASE_DIR = get_base_dir()
TEMPLATE_DIR = os.path.join(BASE_DIR, "template")
OUTPUT_DIR = "generated"


# ===== CORE =====
def replace_placeholders(file_path, data):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    for key, value in data.items():
        content = content.replace(f"{{{{{key.upper()}}}}}", value)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_project(project_name, description, author, template_name):
    # ===== VALIDASI TEMPLATE DIR =====
    if not os.path.exists(TEMPLATE_DIR):
        raise Exception(f"Template directory tidak ditemukan:\n{TEMPLATE_DIR}")

    template_path = os.path.join(TEMPLATE_DIR, template_name)

    if not os.path.exists(template_path):
        available = os.listdir(TEMPLATE_DIR)
        raise Exception(
            f"Template '{template_name}' tidak ditemukan.\n"
            f"Available: {available}"
        )

    # ===== BUAT OUTPUT =====
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, project_name)

    if os.path.exists(output_path):
        raise Exception("Project sudah ada!")

    shutil.copytree(template_path, output_path)

    # ===== DATA =====
    data = {
        "project_name": project_name,
        "description": description,
        "author": author,
    }

    # ===== REPLACE =====
    for root, _, files in os.walk(output_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_placeholders(file_path, data)

    return output_path