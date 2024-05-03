markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
blocks = markdown.strip().split('\n\n')
print(blocks)
blocks = [block.strip() for block in blocks]
print(blocks)
blocks = ['\n'.join(line.strip() for line in block.split('\n')) for block in blocks]
print(blocks)
markdown = """
This is a paragraph with trailing space    

And here's another with leading space 
   This line should be trimmed as well.

   * List with extra indentation
   * Second item with extra space

"""
blocks = markdown.strip().split('\n\n')
print(blocks)
blocks = [block.strip() for block in blocks]
print(blocks)
blocks = ['\n'.join(line.strip() for line in block.split('\n')) for block in blocks]
print(blocks)
markdown = """
This is a paragraph
followed immediately by another line of the same paragraph.

But here's a new block.

* List item
* Another item


* Mistakenly spaced list item
"""
blocks = markdown.strip().split('\n\n')
print(blocks)
blocks = [block.strip() for block in blocks]
print(blocks)
blocks = ['\n'.join(line.strip() for line in block.split('\n')) for block in blocks]
print(blocks)
markdown = """
 First line with a leading space
Second line of the first block
    Third line with indentation that should be removed

Another block starts here and should be cleanly separated from the first
"""
blocks = markdown.strip().split('\n\n')
print(blocks)
blocks = [block.strip() for block in blocks]
print(blocks)
blocks = ['\n'.join(line.strip() for line in block.split('\n')) for block in blocks]
print(blocks)

