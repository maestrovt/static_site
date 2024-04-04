text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

from textnode import TextNode, split_nodes_delimiter

code_node = TextNode("This is text with a `code block` word", text_type_text)
new_code_nodes = split_nodes_delimiter([code_node], "`", text_type_code)
print(new_code_nodes)
bold_node = TextNode("This is text with a **bolded** word", text_type_text)
new_bold_nodes = split_nodes_delimiter([bold_node], "**", text_type_bold)
print(new_bold_nodes)
italic_node = TextNode("This is text with an *italicized* word", text_type_text)
new_italic_nodes = split_nodes_delimiter([italic_node], "*", text_type_italic)
print(new_italic_nodes)
bold_error_node = TextNode("I'm feeling very *special right now!", text_type_text)
new_bold_error_nodes = split_nodes_delimiter([bold_error_node], "*", text_type_italic)
print(new_bold_error_nodes)
