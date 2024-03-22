from htmlnode import HTMLNode

node = HTMLNode("glob", "double_glob", ["glob1", "glob2"], {"href": "https://www.google.com", "target": "_blank"})
print(node)
print(node.props_to_html())