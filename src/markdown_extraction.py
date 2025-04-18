import re
import unittest

def extract_markdown_images(text):
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex, text)
    return matches

def extract_markdown_links(text):
    link_regex = r"(?<!\!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_regex, text)
    return matches

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images_single(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "![alt1](url1) and ![alt2](url2) and some text ![alt3](url3)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("alt1", "url1"), ("alt2", "url2"), ("alt3", "url3")], matches)

    def test_extract_markdown_images_no_images(self):
        text = "This text has no images."
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_images_with_links(self):
        text = "This has a [link](url) and an ![image](img_url)."
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "img_url")], matches)

    def test_extract_markdown_images_empty_alt_text(self):
        text = "![](image_url)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("", "image_url")], matches)

    def test_extract_markdown_images_empty_url(self):
        text = "![alt]()"
        matches = extract_markdown_images(text)
        self.assertListEqual([("alt", "")], matches)

    def test_extract_markdown_links_single(self):
        text = "This is text with a [link](https://www.boot.dev)."
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        text = "[link1](url1) and [link2](url2) and some text [link3](url3)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link1", "url1"), ("link2", "url2"), ("link3", "url3")], matches)

    def test_extract_markdown_links_no_links(self):
        text = "This text has no links."
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links_with_images(self):
        text = "This has an ![image](img_url) and a [link](url)."
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "url")], matches)

    def test_extract_markdown_links_empty_anchor_text(self):
        text = "[](link_url)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("", "link_url")], matches)

    def test_extract_markdown_links_empty_url(self):
        text = "[anchor]()"
        matches = extract_markdown_links(text)
        self.assertListEqual([("anchor", "")], matches)

    def test_extract_markdown_links_and_images_together(self):
        text = "Here's an ![image](image.png) and a [link](boot.dev)!"
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertListEqual([("image", "image.png")], images)
        self.assertListEqual([("link", "boot.dev")], links)

if __name__ == '__main__':
    unittest.main()