class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_strings = []
        for key, value in self.props.items():
            prop_strings.append(f'{key}="{value}"')
        return " " + " ".join(prop_strings) if prop_strings else ""

    def __repr__(self):
        return (f"HTMLNode(tag='{self.tag}', value='{self.value}', "
                f"children={self.children}, props={self.props})")

