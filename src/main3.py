from leafnode import LeafNode

node1 = LeafNode("p", "This is a paragraph of text.")
node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
node3 = LeafNode(None, "Normal text")
print(node1)
print(node1.to_html())
print(node2)
print(node2.to_html())
print(node3)
print(node3.to_html())
