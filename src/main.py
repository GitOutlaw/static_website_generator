import os
import shutil
from pathlib import Path

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Crawls every entry in the content directory.
    For each markdown file found, generates a new .html file using the same template.html.
    The generated pages are written to the public directory in the same directory structure.
    """
    content_path = Path(dir_path_content)
    public_path = Path(dest_dir_path)

    for item in content_path.rglob("*"):
        if item.is_file() and item.suffix == ".md":
            relative_path = item.relative_to(content_path)
            output_path = public_path / relative_path.with_suffix(".html")
            generate_page(str(item), template_path, str(output_path))


def main():
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
    copy_files_recursive(dir_path_static, dir_path_public)
    print(f"Copied static files from '{dir_path_static}' to '{dir_path_public}'")

    print("Generating pages recursively...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    print(f"Generated HTML pages in '{dir_path_public}'")


if __name__ == "__main__":
    main()