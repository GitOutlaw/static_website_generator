import os
from textnode import markdown_to_html_node, TextNode, TextType


def extract_title(markdown):
    """Extract the h1 header from Markdown, raise ValueError if not found."""
    lines = markdown.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found in Markdown")


def generate_page(from_path, template_path, dest_path):
    """Generate an HTML page from a Markdown file using a template."""
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read Markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read template file
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Convert Markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Replace placeholders in template
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write output to destination
    with open(dest_path, 'w') as f:
        f.write(final_html)