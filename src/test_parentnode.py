import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        children = [
            LeafNode("b", "bold"),
            LeafNode(None, "normal"),
            LeafNode("i", "italic"),
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(parent_node.to_html(), "<p><b>bold</b>normal<i>italic</i></p>")

    def test_to_html_nested_parent_nodes(self):
        inner_parent = ParentNode("ul", [LeafNode("li", "item")])
        outer_parent = ParentNode("div", [inner_parent])
        self.assertEqual(outer_parent.to_html(), "<div><ul><li>item</li></ul></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_creation_without_tag_raises_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("span", "child")])
        self.assertEqual(str(context.exception), "ParentNode must have a tag.")

    def test_creation_without_children_raises_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None)
        self.assertEqual(str(context.exception), "ParentNode must have children.")

    def test_creation_with_non_list_children_raises_type_error(self):
        with self.assertRaises(TypeError) as context:
            ParentNode("div", "not a list")
        self.assertEqual(str(context.exception), "children must be a list.")

    def test_to_html_empty_children_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_nested_parents_with_text_nodes(self):
        parent1 = ParentNode("div", [LeafNode(None, "Text 1")])
        parent2 = ParentNode("p", [parent1, LeafNode(None, "Text 2")])
        self.assertEqual(parent2.to_html(), "<p><div>Text 1</div>Text 2</p>")

if __name__ == '__main__':
    unittest.main()