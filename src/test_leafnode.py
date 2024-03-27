import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual('LeafNode(p, This is a paragraph of text., None)',repr(node))

if __name__ == "__main__":
    unittest.main()
