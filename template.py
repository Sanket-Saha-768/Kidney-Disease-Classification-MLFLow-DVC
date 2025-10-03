"""
Project Template Generator

This script creates the standard folder and file structure
for ML/DL projects (with config, src, tests, data, etc.).
"""


import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = input("Enter project name:") 

list_of_files = [
    # GitHub Actions workflow
    ".github/workflows/.gitkeep",

    # Source code structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",

    # Configuration files
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",

    # Project setup files
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",

    # Research & experimentation
    "notebooks/trials.ipynb",

    # Web templates (if you plan inference service with Flask/FastAPI)
    "templates/index.html",
    "app.py",

    # Main pipeline entry
    "main.py",

    # Testing
    "tests/__init__.py",
    "tests/test_sample.py",

    # Data directories
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/artifacts/.gitkeep",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
