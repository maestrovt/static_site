import unittest
from inline_markdown import markdown_to_blocks
from markdown_blocks import (block_to_block_type,
                             block_type_olist,
                             block_type_code,
                             block_type_heading,
                             block_type_paragraph,
                             block_type_quote,
                             block_type_ulist,
                             paragraph_to_html_node,
                             markdown_to_html_node
                            )
from markdown_blocks_bd import block_type_olist, block_type_ulist
from parentnode import ParentNode
from leafnode import LeafNode


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    def test_block_to_block_type(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

# Heading 1

###### Heading 6

```
This is code.
```

>Quote line 1
>Quote line 2
>Quote line 3
Line 4, no quote!

* This is a list
* with items

- This is another list
* With other items
But one line is missing the unordered list character

1. Priority A
2. Priority B

1. Another list
2. This line is numbered
But this line is not
"""
        correct_block_type_list = [
            block_type_paragraph,
            block_type_paragraph,
            block_type_heading,
            block_type_heading,
            block_type_code,
            block_type_paragraph,
            block_type_ulist,
            block_type_paragraph,
            block_type_olist,
            block_type_paragraph
        ]
        blocks = markdown_to_blocks(markdown)
        block_type_list = []
        for block in blocks:
            block_type_list.append(block_to_block_type(block))
        self.assertListEqual(block_type_list, correct_block_type_list)
    def test_block_to_block_types_bd(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    def test_markdown_to_html(self):
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
        blocks = markdown_to_blocks(markdown)
        node_0 = markdown_to_html_node(blocks[0])
        html_0 = node_0.to_html()
        str_0 = "<div><p>This is a <b>bolded</b> paragraph</p></div>"
        self.assertEqual(str_0, html_0)
        node_1 = markdown_to_html_node(blocks[1])
        html_1 = node_1.to_html()
        str_1 = '<div><p>This is another paragraph with <i>italic</i> text and <code>code</code> here This is the same paragraph on a new line This is text with a <a href="https://boot.dev">link</a> and <a href="https://blog.boot.dev">another link</a> with text that follows This is <b>text</b> with an <i>italic</i> word and a <code>code block</code> and an <img src="https://i.imgur.com/zjjcJKZ.png" alt="image"></img> and a <a href="https://boot.dev">link</a></p></div>'
        self.assertEqual(str_1, html_1)
        node_2 = markdown_to_html_node(blocks[2])
        html_2 = node_2.to_html()
        str_2 = '<div><h1>Heading 1</h1></div>'
        self.assertEqual(str_2, html_2)
        node_3 = markdown_to_html_node(blocks[3])
        html_3 = node_3.to_html()
        str_3 = '<div><h2>Heading 2</h2></div>'
        self.assertEqual(str_3, html_3)
        node_4 = markdown_to_html_node(blocks[4])
        html_4 = node_4.to_html()
        str_4 = '<div><h3>Heading 3</h3></div>'
        self.assertEqual(str_4, html_4)
        node_5 = markdown_to_html_node(blocks[5])
        html_5 = node_5.to_html()
        str_5 = '<div><h4>Heading 4</h4></div>'
        self.assertEqual(str_5, html_5)
        node_6 = markdown_to_html_node(blocks[6])
        html_6 = node_6.to_html()
        str_6 = '<div><h5>Heading 5</h5></div>'
        self.assertEqual(str_6, html_6)
        node_7 = markdown_to_html_node(blocks[7])
        html_7 = node_7.to_html()
        str_7 = '<div><h6>Heading 6</h6></div>'
        self.assertEqual(str_7, html_7)
        node_8 = markdown_to_html_node(blocks[8])
        html_8 = node_8.to_html()
        str_8 = """<div><pre><code>This is code.
This is more code.
This is even more code.
</code></pre></div>"""
        self.assertEqual(str_8, html_8)
        node_9 = markdown_to_html_node(blocks[9])
        html_9 = node_9.to_html()
        str_9 = "<div><blockquote>Quote line 1 Quote line 2 Quote line 3 Line 4, no quote!</blockquote></div>"
        self.assertEqual(str_9, html_9)
        node_10 = markdown_to_html_node(blocks[10])
        html_10 = node_10.to_html()
        str_10 = "<div><ul><li>This is a list</li><li>with items</li></ul></div>"
        self.assertEqual(str_10, html_10)
        node_11 = markdown_to_html_node(blocks[11])
        html_11 = node_11.to_html()
        str_11 = "<div><ul><li>This is another list</li><li>With other items</li><li>But one line is missing the unordered list character</li></ul></div>"
        self.assertEqual(str_11, html_11)
        node_12 = markdown_to_html_node(blocks[12])
        html_12 = node_12.to_html()
        str_12 =  "<div><ol><li>Priority A</li><li>Priority B</li><li>Priority C</li></ol></div>"
        self.assertEqual(str_12, html_12)
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        str = """<div><p>This is a <b>bolded</b> paragraph</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here This is the same paragraph on a new line This is text with a <a href="https://boot.dev">link</a> and <a href="https://blog.boot.dev">another link</a> with text that follows This is <b>text</b> with an <i>italic</i> word and a <code>code block</code> and an <img src="https://i.imgur.com/zjjcJKZ.png" alt="image"></img> and a <a href="https://boot.dev">link</a></p><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6><pre><code>This is code.
This is more code.
This is even more code.
</code></pre><blockquote>Quote line 1 Quote line 2 Quote line 3 Line 4, no quote!</blockquote><ul><li>This is a list</li><li>with items</li></ul><ul><li>This is another list</li><li>With other items</li><li>But one line is missing the unordered list character</li></ul><ol><li>Priority A</li><li>Priority B</li><li>Priority C</li></ol></div>"""
        self.assertEqual(str, html)
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )



if __name__ == "__main__":
    unittest.main()