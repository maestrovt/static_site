import re

from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
from parentnode import ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

# Convert full markdown document to a list of "block" strings
# Split input string into distinct blocks and strip and leading or trailing whitespace
# Remove any "empty" blocks due to excessive newlines
# Called by markdown_to_html_node

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

# Convert full markdown document to ParentNode with "div" tag
# Top level function
# Calls markdown_to_blocks and block_to_html_node 

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

# Convert block to html_node according to block type
# Called by markdown_to_html_node
# Calls block_to_block_type
# Calls x_to_html_node for block_type x


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

# Returns block type of block
# Called by block_to_html_node

def block_to_block_type(block):
    for i in range(1, 7):
        if block.startswith('#' * i + ' '):
            return block_type_heading
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    if block.startswith('>'):
        lines = block.splitlines()
        all_start_with_quote_character = True
        for line in lines:
            if not line.startswith('>'):
                all_start_with_quote_character = False
        if all_start_with_quote_character:
            return block_type_quote
    if block.startswith('* ') or block.startswith('- '):
        lines = block.splitlines()
        all_start_with_unordered_list_character = True
        for line in lines:
            if not (line.startswith('* ') or line.startswith('- ')):
                all_start_with_unordered_list_character = False
        if all_start_with_unordered_list_character:
            return block_type_ulist
    match = re.search(r'^\d+\.\s', block)
    if match:
        # Compile a regular expression pattern that matches a number followed by a period and a space at the start of a string
        pattern = re.compile(r'^\d+\.\s', re.MULTILINE)

        # Find all matches; if every line matches, the block is an ordered list
        matches = pattern.findall(block)
    
        # Split the block into lines
        lines = block.splitlines()

         # Check if the number of matches equals the number of lines
        if len(matches) == len(lines):
            return block_type_olist
    return block_type_paragraph

# Creates a list of TextNodes from an input string
# Input string has had "\n" removed
# List of TextNodes converted to LeafNodes
# Returns a list of children LeafNodes
# Called by x_to_html_node according to block type


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def ulist_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def olist_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code_node = ParentNode("code", children)
    return ParentNode("pre", [code_node])


 




 