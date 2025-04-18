# src/main.py
import os
import shutil
import sys
from pathlib import Path

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"  # Always build to docs for deployment
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print(f"Building site with basepath: '{basepath}' to directory: '{dir_path_public}'")

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        print(f"Deleted: {dir_path_public}")
    else:
        print(f"Public directory '{dir_path_public}' does not exist, skipping deletion.")

    print("Creating public directory...")
    os.makedirs(dir_path_public, exist_ok=True)
    print(f"Created: {dir_path_public}")

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, os.path.join(dir_path_public, "static")) # Copy static to /docs/static
    print(f"Copied static files from '{dir_path_static}' to '{os.path.join(dir_path_public, 'static')}'")

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
    print(f"Generated HTML pages in '{dir_path_public}' with basepath: '{basepath}'")


if __name__ == "__main__":
    main()