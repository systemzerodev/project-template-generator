import os
import shutil
import json

TEMPLATE_DIR = "template"

def replace_placeholders(file_path, data):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    for key, value in data.items():
        content = content.replace(f"{{{{{key.upper()}}}}}", value)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_project():
    with open("config.json", "r") as f:
        config = json.load(f)

    project_name = config["project_name"]

    shutil.copytree(TEMPLATE_DIR, project_name)

    for root, _, files in os.walk(project_name):
        for file in files:
            file_path = os.path.join(root, file)
            replace_placeholders(file_path, config)

    print(f"Project '{project_name}' berhasil dibuat!")


if __name__ == "__main__":
    generate_project()