import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "template")


def generate_project(name, desc, author, template_name):
    template_path = os.path.join(TEMPLATE_DIR, template_name)

    if not os.path.exists(template_path):
        raise Exception(f"Template '{template_name}' tidak ditemukan")

    output_dir = os.path.join(os.getcwd(), "generated", name)

    if os.path.exists(output_dir):
        raise Exception("Project sudah ada")

    shutil.copytree(template_path, output_dir)

    for root, _, files in os.walk(output_dir):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                content = content.replace("{{PROJECT_NAME}}", name)
                content = content.replace("{{DESCRIPTION}}", desc)
                content = content.replace("{{AUTHOR}}", author)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

            except:
                pass

    return output_dir