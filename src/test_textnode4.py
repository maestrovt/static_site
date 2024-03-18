import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.deathstar.com")
        self.assertEqual("TextNode(This is a text node, bold, https://www.deathstar.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
