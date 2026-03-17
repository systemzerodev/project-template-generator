import os
import shutil
import importlib.util


# ================================
# PATH RESOLVER (WORK DI SEMUA ENV)
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
# CEK FILE TEXT ATAU BINARY
# ================================
def is_text_file(file_path):
    try:
        with open(file_path, "rb") as f:
            chunk = f.read(1024)
            if b"\x00" in chunk:
                return False
        return True
    except:
        return False


# ================================
# READ FILE (ANTI ERROR ENCODING)
# ================================
def read_file_safe(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        try:
            with open(file_path, "r", encoding="latin-1", errors="ignore") as f:
                return f.read()
        except:
            print(f"[SKIP READ] {file_path}")
            return None


# ================================
# WRITE FILE (SAFE)
# ================================
def write_file_safe(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except:
        print(f"[SKIP WRITE] {file_path}")


# ================================
# REPLACE PLACEHOLDER
# ================================
def replace_placeholders(file_path, data):
    if not is_text_file(file_path):
        return

    content = read_file_safe(file_path)

    if content is None:
        return

    for key, value in data.items():
        content = content.replace(f"{{{{{key.upper()}}}}}", value)

    write_file_safe(file_path, content)


# ================================
# MAIN GENERATOR
# ================================
def generate_project(project_name, description, author, template_name):
    # === VALIDASI TEMPLATE DIR ===
    if not os.path.exists(TEMPLATE_DIR):
        raise Exception(f"Template directory tidak ditemukan:\n{TEMPLATE_DIR}")

    template_path = os.path.join(TEMPLATE_DIR, template_name)

    if not os.path.exists(template_path):
        available = os.listdir(TEMPLATE_DIR)
        raise Exception(
            f"Template '{template_name}' tidak ditemukan.\nAvailable: {available}"
        )

    # === OUTPUT DIR ===
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, project_name)

    if os.path.exists(output_path):
        raise Exception(f"Project '{project_name}' sudah ada!")

    # === COPY TEMPLATE ===
    shutil.copytree(template_path, output_path)

    # === DATA PLACEHOLDER ===
    data = {
        "project_name": project_name,
        "description": description,
        "author": author,
    }

    # === PROCESS FILE ===
    for root, _, files in os.walk(output_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_placeholders(file_path, data)

    return output_path