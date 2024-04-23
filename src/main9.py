from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)
def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
print(text_to_textnodes(text))
text1 = "This is an *italic* word with a **bold** text and an ![image](https:/glob.com/image.png) and a `code block` and a [link](https://deathstar.com) and a bit more text."
print(text_to_textnodes(text1))