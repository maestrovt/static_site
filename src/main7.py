from inline_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, text_type_text

node = TextNode("Text1 ![img1](https://url1.com/media/img1.png) text2 ![img2](https://url2.com/media/img2.png)",
                text_type_text
                )
new_nodes = split_nodes_image([node])
print(new_nodes)
node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
new_nodes = split_nodes_image([node])
print(new_nodes)
node = TextNode(
    "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
    text_type_text,
)
new_nodes = split_nodes_link([node])
print(new_nodes)