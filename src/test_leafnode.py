import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Visit Google", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Visit Google</a>')

    def test_leaf_to_html_span_with_class(self):
        node = LeafNode("span", "Important text", {"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Important text</span>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw text here")
        self.assertEqual(node.to_html(), "Raw text here")

    def test_leaf_creation_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None)

    def test_leaf_creation_with_children_raises_type_error(self):
        with self.assertRaises(TypeError):
            LeafNode("div", "Text", children=[HTMLNode("span", "Child")])

    def test_leaf_to_html_empty_value_within_tag(self):
        node = LeafNode("div", "")
        self.assertEqual(node.to_html(), "<div></div>")

if __name__ == '__main__':
    unittest.main()