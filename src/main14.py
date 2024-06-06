from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_quote,
    block_type_ulist,
    block_type_olist,
    block_type_code,
    block_type_heading,
)
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_type_text, text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from markdown_blocks import (
    paragraph_to_html_node,
    quote_to_html_node,
    ulist_to_html_node,
    olist_to_html_node,
    code_to_html_node,
    heading_to_html_node,
    markdown_to_html_node
)

markdown = """
This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line
This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows
This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

```
This is code.
This is more code.
This is even more code.
```

>Quote line 1
>Quote line 2
>Quote line 3
>Line 4, no quote!

* This is a list
* with items

- This is another list
- With other items
- But one line is missing the unordered list character

1. Priority A
2. Priority B
3. Priority C
"""

print(markdown_to_html_node(markdown).to_html())
