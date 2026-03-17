from setuptools import setup, find_packages

setup(
    name="project-generator",
    version="0.1.0",
    description="CLI tool to generate project templates with UI",
    author="FullstackDev",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["template/*"],
    },
    entry_points={
        "console_scripts": [
            "create-project=project_generator.ui:run",
        ],
    },
    python_requires=">=3.8",
)