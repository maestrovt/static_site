from markdown_blocks import markdown_to_blocks, block_to_block_type

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
"""
blocks = markdown_to_blocks(markdown)
print(blocks)
for block in blocks:
    print(block_to_block_type(block))
