from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.children:
            raise ValueError("LeafNode cannot have children.")

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to render HTML.")
        if self.tag is None:
            return self.value
        else:
            props_str = self.props_to_html()
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag='{self.tag}', value='{self.value}', props={self.props})"

if __name__ == '__main__':
    paragraph = LeafNode("p", "This is a paragraph.")
    link = LeafNode("a", "Click here", {"href": "https://example.com"})
    raw_text = LeafNode(None, "Just some plain text")

    print(paragraph)
    print(link)
    print(raw_text)
    print(paragraph.to_html())
    print(link.to_html())
    print(raw_text.to_html())

    try:
        invalid_node_no_value = LeafNode("span", None)
    except ValueError as e:
        print(f"Error creating invalid node: {e}")

    try:
        invalid_node_with_children = LeafNode("div", "Text", children=[HTMLNode("span", "Child")])
    except ValueError as e:
        print(f"Error creating invalid node: {e}")