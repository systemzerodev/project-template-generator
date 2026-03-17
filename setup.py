from setuptools import setup, find_packages

setup(
    name="project-generator",
    version="0.1.0",
    description="A simple project template generator with CLI and GUI",
    author="Systemzerodev",
    packages=find_packages(),

    include_package_data=True,  # 🔥 penting untuk template & assets

    install_requires=[],

    entry_points={
        "console_scripts": [
            "create-project=project_generator.cli:main",
        ],
    },

    python_requires=">=3.8",
)