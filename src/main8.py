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
def text_to_textnodes(text, new_nodes = None):
    if new_nodes is None:
        new_nodes = []
    bold_pos = text.find('**') if '**' in text else float('inf')
    italic_pos = text.find('*') if '*' in text else float('inf')
    code_pos = text.find('`') if '`' in text else float('inf')
    image_pos = text.find('![image]') if '![image]' in text else float('inf')
    link_pos = text.find('[link]') if '[link]' in text else float('inf')
    text_node = TextNode(text, text_type_text)
    first_pos = min(bold_pos, italic_pos, code_pos, image_pos, link_pos)

    if first_pos == bold_pos:
        split_nodes = split_nodes_delimiter([text_node], "**", text_type_bold)
        new_nodes.extend(split_nodes[:2])
        if len(split_nodes) > 2:
            text_to_textnodes(split_nodes[2].text, new_nodes)
    elif first_pos == italic_pos:
        split_nodes = split_nodes_delimiter([text_node], "*", text_type_italic)
        new_nodes.extend(split_nodes[:2])
        if len(split_nodes) > 2:
            text_to_textnodes(split_nodes[2].text, new_nodes)
    elif first_pos == code_pos:
        split_nodes = split_nodes_delimiter([text_node], "`", text_type_code)
        new_nodes.extend(split_nodes[:2])
        if len(split_nodes) > 2:
            text_to_textnodes(split_nodes[2].text, new_nodes)
    elif first_pos == image_pos:
        split_nodes = split_nodes_image([text_node])
        new_nodes.extend(split_nodes[:2])
        if len(split_nodes) > 2:
            text_to_textnodes(split_nodes[2].text, new_nodes)
    elif first_pos == link_pos:
        split_nodes = split_nodes_link([text_node])
        new_nodes.extend(split_nodes[:2])
        if len(split_nodes) > 2:
            text_to_textnodes(split_nodes[2].text, new_nodes)
    else:
        new_nodes.append(text_node)
    return new_nodes


text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
print(text_to_textnodes(text))
text1 = "This is an *italic* word with a **bold** text and an ![image](https:/glob.com/image.png) and a `code block` and a [link](https://deathstar.com) and a bit more text."
print(text_to_textnodes(text1))