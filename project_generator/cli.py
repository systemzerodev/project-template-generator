import argparse
from project_generator.generator import generate_project


def main():
    parser = argparse.ArgumentParser(description="Project Generator")

    parser.add_argument("name", nargs="?", help="Project name")  # 🔥 FIX DI SINI
    parser.add_argument("--desc", default="", help="Description")
    parser.add_argument("--author", default="Systemzerodev", help="Author")
    parser.add_argument("--template", default="python", help="Template")

    args = parser.parse_args()

    # ===== MODE UI =====
    if not args.name:
        from project_generator.ui import run
        run()
        return

    # ===== MODE CLI =====
    try:
        path = generate_project(
            args.name,
            args.desc,
            args.author,
            args.template
        )

        print(f"\n✅ Project created at: {path}")

    except Exception as e:
        print(f"\n❌ Error: {e}")