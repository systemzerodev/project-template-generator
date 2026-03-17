from setuptools import setup, find_packages

setup(
    name="project-generator",
    version="0.1.0",
    description="A simple project template generator with CLI and GUI",
    author="Systemzerodev",
    packages=find_packages(),

    # 🔥 penting untuk include file non-python
    include_package_data=True,

    # 🔥 CLI command
    entry_points={
        "console_scripts": [
            "create-project=project_generator.cli:main",
        ],
    },

    # opsional tapi bagus
    install_requires=[],
    python_requires=">=3.8",

    # metadata tambahan
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)