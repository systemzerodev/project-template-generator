import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIR = os.path.join(BASE_DIR, "template")
OUTPUT_DIR = os.path.join(BASE_DIR, "generated")


def replace_placeholders(file_path, data):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    for key, value in data.items():
        content = content.replace(f"{{{{{key.upper()}}}}}", value)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_project(project_name, description, author):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, project_name)

    if os.path.exists(output_path):
        raise Exception("Project sudah ada!")

    shutil.copytree(TEMPLATE_DIR, output_path)

    data = {
        "project_name": project_name,
        "description": description,
        "author": author
    }

    for root, _, files in os.walk(output_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_placeholders(file_path, data)

    return output_path