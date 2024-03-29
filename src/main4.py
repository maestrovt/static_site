from leafnode import LeafNode
from parentnode import ParentNode
node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    {"class": "greeting", "href": "https://boot.dev"},
)

node2 = ParentNode(
            "div",
            [LeafNode(None, "Normal text"),
             LeafNode("p", "Hello, world!"),
             ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            ],
            {"class": "greeting", "href": "https://boot.dev"},
)
node3 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
print(node.to_html())
print(node2.to_html())
print(node3.to_html())
