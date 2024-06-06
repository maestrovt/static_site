from markdown_blocks_bd import (
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
from textnode import text_node_to_html_node
from leafnode import LeafNode

markdown = """
This is **bolded** paragraph

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
blocks = markdown_to_blocks(markdown)
for block in blocks:
    print(block_to_block_type(block))
    if block_to_block_type(block) == block_type_paragraph:
        nodes = text_to_textnodes(block)
        html = "<p>\n"
        for node in nodes:
            html_node = text_node_to_html_node(node)
            html += html_node.to_html()
        html += "\n</p"
        print(html)
    if block_to_block_type(block) == block_type_quote:
        lines = block.splitlines()
        cleaned_lines = [line.lstrip(">") for line in lines]
        cleaned_block = "\n".join(cleaned_lines)
        nodes = text_to_textnodes(cleaned_block)
        html = "<blockquote>\n"
        for node in nodes:
            html_node = text_node_to_html_node(node)
            html += html_node.to_html()
        html += "\n</blockquote>"
        print(html)
    if block_to_block_type(block) == block_type_ulist:
        lines = block.splitlines()
        cleaned_lines = [line.lstrip('*- ') for line in lines]
        cleaned_lines = ["\t<li>"+line+"</li>" for line in cleaned_lines]
        cleaned_block = '\n'.join(cleaned_lines)
        nodes = text_to_textnodes(cleaned_block)
        html = "<ul>\n"
        for node in nodes:
            html_node = text_node_to_html_node(node)
            html += html_node.to_html()
        html += "\n</ul>"
        print(html)
    if block_to_block_type(block) == block_type_olist:
        lines = block.splitlines()
        cleaned_lines = []
        for i in range(1, len(lines)+1):
            line = lines[i-1].lstrip(f"{i}. ")
            li_line = "\t<li>"+line+"</li>"
            cleaned_lines.append(li_line)
        cleaned_block = "\n".join(cleaned_lines)
        nodes = text_to_textnodes(cleaned_block)
        html = "<ol>\n"
        for node in nodes:
            html_node = text_node_to_html_node(node)
            html += html_node.to_html()
        html += "\n</ol>"
        print(html)
    if block_to_block_type(block) == block_type_code:
        cleaned_block = block.lstrip("```")
        cleaned_block = cleaned_block.rstrip("```")
        nodes = text_to_textnodes(cleaned_block)
        html = "<pre><code>"
        for node in nodes:
            html_node = text_node_to_html_node(node)
            html += html_node.to_html()
        html += "</code></pre>"
        print(html)
    if block_to_block_type(block) == block_type_heading:
        if block.startswith("# "):
            cleaned_block = block.lstrip("# ")
            nodes = text_to_textnodes(cleaned_block)
            html = "<h1>"
            for node in nodes:
                html_node = text_node_to_html_node(node)
                html += html_node.to_html()
            html += "</h1>"
            print(html)
        if block.startswith("## "):
            cleaned_block = block.lstrip("## ")
            nodes = text_to_textnodes(cleaned_block)
            html = "<h2>"
            for node in nodes:
                html_node = text_node_to_html_node(node)
                html += html_node.to_html()
            html += "</h2>"
            print(html)
        if block.startswith("### "):
            cleaned_block = block.lstrip("### ")
            nodes = text_to_textnodes(cleaned_block)
            html = "<h3>"
            for node in nodes:
                html_node = text_node_to_html_node(node)
                html += html_node.to_html()
            html += "</h3>"
            print(html)
        if block.startswith("#### "):
            cleaned_block = block.lstrip("#### ")
            nodes = text_to_textnodes(cleaned_block)
            html = "<h4>"
            for node in nodes:
                html_node = text_node_to_html_node(node)
                html += html_node.to_html()
            html += "</h4>"
            print(html)
        if block.startswith("##### "):
            cleaned_block = block.lstrip("##### ")
            nodes = text_to_textnodes(cleaned_block)
            html = "<h5>"
            for node in nodes:
                html_node = text_node_to_html_node(node)
                html += html_node.to_html()
            html += "</h5>"
            print(html)
        if block.startswith("###### "):
            cleaned_block = block.lstrip("###### ")
            nodes = text_to_textnodes(cleaned_block)
            html = "<h6>"
            for node in nodes:
                html_node = text_node_to_html_node(node)
                html += html_node.to_html()
            html += "</h6>"
            print(html)
