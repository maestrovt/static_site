import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("glob", "double_glob", ["glob1", "glob2"], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())
    def test_repr(self):
        node = HTMLNode("glob", "double_glob", ["glob1", "glob2"], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual('HTMLNode(tag = glob, value = double_glob, children = glob1, glob2, props = href="https://www.google.com" target="_blank")',repr(node))

if __name__ == "__main__":
    unittest.main()
