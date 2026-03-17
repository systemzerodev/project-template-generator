from setuptools import setup, find_packages

setup(
    name="project-generator",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "create-project=project_generator.ui:run",
        ],
    },
)