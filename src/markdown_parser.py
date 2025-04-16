from enum import Enum
import unittest


class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4


class TextNode:
    def __init__(self, text, text_type):
        self.text = text
        self.text_type = text_type

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type

    def __repr__(self):
        return f"TextNode('{self.text}', TextType.{self.text_type.name})"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(
                f"Mismatched delimiter '{delimiter}' in text: '{node.text}'")

        for i, part in enumerate(parts):
            if part:  # Only add non-empty parts
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        nodes = [TextNode("This is plain text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            result, [TextNode("This is plain text", TextType.TEXT)])

    def test_single_delimiter_pair(self):
        nodes = [
            TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ])

    def test_multiple_delimiter_pairs(self):
        nodes = [TextNode("This has **two** bold **sections**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This has ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" bold ", TextType.TEXT),
            TextNode("sections", TextType.BOLD)
        ])

    def test_delimiter_at_start_and_end(self):
        nodes = [TextNode("**bold text**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("bold text", TextType.BOLD)
        ])

    def test_delimiter_surrounding_text(self):
        nodes = [TextNode("prefix**bold**suffix", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("prefix", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("suffix", TextType.TEXT)
        ])

    def test_code_delimiter(self):
        nodes = [TextNode("This has `some code` in it", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This has ", TextType.TEXT),
            TextNode("some code", TextType.CODE),
            TextNode(" in it", TextType.TEXT)
        ])

    def test_italic_delimiter(self):
        nodes = [TextNode("This has _italic text_", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("This has ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC)
        ])

    def test_text_node_remains_unchanged(self):
        nodes = [TextNode("Plain text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(result, [TextNode("Plain text", TextType.TEXT)])

    def test_non_text_node_remains_unchanged(self):
        nodes = [TextNode("Bold text", TextType.BOLD)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [TextNode("Bold text", TextType.BOLD)])

        nodes = [TextNode("Italic text", TextType.ITALIC)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(result, [TextNode("Italic text", TextType.ITALIC)])

        nodes = [TextNode("Code text", TextType.CODE)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [TextNode("Code text", TextType.CODE)])

    def test_mismatched_delimiter(self):
        nodes = [TextNode("This has a *single asterisk", TextType.TEXT)]
        with self.assertRaisesRegex(ValueError, r"Mismatched delimiter '\*' in text: 'This has a \*single asterisk'"):
            split_nodes_delimiter(nodes, "*", TextType.ITALIC)

        nodes = [TextNode("This has an open **bold", TextType.TEXT)]
        with self.assertRaisesRegex(ValueError, r"Mismatched delimiter '\*\*' in text: 'This has an open \*\*bold'"):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

        nodes = [TextNode("This has a closing bold**", TextType.TEXT)]
        with self.assertRaisesRegex(ValueError, r"Mismatched delimiter '\*\*' in text: 'This has a closing bold\*\*'"):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_empty_delimiter(self):
        nodes = [TextNode("test", TextType.TEXT)]
        with self.assertRaisesRegex(ValueError, r"empty separator"):
            split_nodes_delimiter(nodes, "", TextType.BOLD)

    def test_multiple_nodes_input(self):
        nodes = [
            TextNode("This has ", TextType.TEXT),
            TextNode("**bold**", TextType.TEXT),
            TextNode(" and `code`.", TextType.TEXT)
        ]
        result_bold = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result_bold, [
            TextNode("This has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and `code`.", TextType.TEXT)
        ])

        result_code = split_nodes_delimiter(result_bold, "`", TextType.CODE)
        self.assertEqual(result_code, [
            TextNode("This has ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT)
        ])


if __name__ == '__main__':
    unittest.main()
