from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """Converts a TextNode to a LeafNode."""
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")

if __name__ == '__main__':
    text = TextNode("Plain text", TextType.TEXT)
    bold = TextNode("Bold!", TextType.BOLD)
    italic = TextNode("Italic!", TextType.ITALIC)
    code = TextNode("print('hello')", TextType.CODE)
    link = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
    image = TextNode("Boot.dev logo", TextType.IMAGE, "logo.png")
    unknown = TextNode("Unknown", "UNKNOWN")

    print(text_node_to_html_node(text))
    print(text_node_to_html_node(bold))
    print(text_node_to_html_node(italic))
    print(text_node_to_html_node(code))
    print(text_node_to_html_node(link))
    print(text_node_to_html_node(image))

    try:
        text_node_to_html_node(unknown)
    except ValueError as e:
        print(f"Error: {e}")