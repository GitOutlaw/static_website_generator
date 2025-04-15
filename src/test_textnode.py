import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_equal_nodes(self):
        node1 = TextNode("Same text", TextType.TEXT)
        node2 = TextNode("Same text", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_equal_nodes_with_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("Text one", TextType.TEXT)
        node2 = TextNode("Text two", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Some text", TextType.BOLD)
        node2 = TextNode("Some text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Link", TextType.LINK, "http://url1.com")
        node2 = TextNode("Link", TextType.LINK, "http://url2.com")
        self.assertNotEqual(node1, node2)

    def test_equal_nodes_with_none_url(self):
        node1 = TextNode("No link", TextType.TEXT, None)
        node2 = TextNode("No link", TextType.TEXT)  # Default url is None
        self.assertEqual(node1, node2)

    def test_not_equal_one_url_none(self):
        node1 = TextNode("Link", TextType.LINK, "http://example.com")
        node2 = TextNode("Link", TextType.LINK)  # Default url is None
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()