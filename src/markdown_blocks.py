import re
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

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
            return block_type_unordered_list
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
            return block_type_ordered_list

    return block_type_paragraph
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks