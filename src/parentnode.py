from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if children is None:
            raise ValueError("ParentNode must have children.")
        if not isinstance(children, list):
            raise TypeError("children must be a list.")
        super().__init__(tag=tag, children=children, props=props)
        self.value = None  # ParentNode doesn't have a direct value

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to render HTML.")
        if self.children is None:
            raise ValueError("ParentNode must have children to render HTML.")

        children_html = "".join(child.to_html() for child in self.children)
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag='{self.tag}', children={self.children}, props={self.props})"

if __name__ == '__main__':
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(node)
    print(node.to_html())

    nested_node = ParentNode(
        "div",
        [
            LeafNode("span", "Outer"),
            ParentNode("ul", [LeafNode("li", "Item 1"), LeafNode("li", "Item 2")]),
            LeafNode("span", "Inner"),
        ],
        {"class": "container"},
    )
    print(nested_node)
    print(nested_node.to_html())

    try:
        invalid_node_no_tag = ParentNode(None, [LeafNode("span", "child")])
    except ValueError as e:
        print(f"Error creating invalid node: {e}")

    try:
        invalid_node_no_children = ParentNode("div", None)
    except ValueError as e:
        print(f"Error creating invalid node: {e}")