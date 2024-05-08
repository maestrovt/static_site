import unittest
from inline_markdown import markdown_to_blocks
from markdown_blocks import (block_to_block_type,
                             block_type_ordered_list,
                             block_type_code,
                             block_type_heading,
                             block_type_paragraph,
                             block_type_quote,
                             block_type_unordered_list,
                            )


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
            block_type_unordered_list,
            block_type_paragraph,
            block_type_ordered_list,
            block_type_paragraph
        ]
        blocks = markdown_to_blocks(markdown)
        block_type_list = []
        for block in blocks:
            block_type_list.append(block_to_block_type(block))
        self.assertListEqual(block_type_list, correct_block_type_list)


if __name__ == "__main__":
    unittest.main()