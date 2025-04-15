import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_multiple_props(self):
        node = HTMLNode(tag="img", props={"src": "image.png", "alt": "An image"})
        expected = ' src="image.png" alt="An image"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_with_spaces_in_values(self):
        node = HTMLNode(tag="div", props={"class": "main container"})
        self.assertEqual(node.props_to_html(), ' class="main container"')

    def test_no_props_is_empty_string(self):
        node1 = HTMLNode(tag="p", value="Some text")
        node2 = HTMLNode(tag="h1", children=[HTMLNode(value="Title")])
        self.assertEqual(node1.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), "")

if __name__ == '__main__':
    unittest.main()