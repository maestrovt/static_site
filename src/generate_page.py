import os
from markdown_blocks import markdown_to_blocks, markdown_to_html_node, block_to_block_type, block_type_heading
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            if block.startswith('# '):
                title = block[1:]
                return title
    if not title:
        raise Exception("All pages need a single h1 header")
    

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    list = os.listdir(dir_path_content)
    if len(list) == 0:
        return
    for item in list:
        content_path = os.path.join(dir_path_content, item)
        if os.path.isfile(content_path):
            if item.endswith('.md'):
                base_name = os.path.splitext(item)[0]
                new_filename = base_name + '.html'
                dest_path = os.path.join(dest_dir_path, new_filename)
                generate_page(content_path, template_path, dest_path)
        else:
            content_dir = os.path.join(dir_path_content, item)
            dest_dir = os.path.join(dest_dir_path, item)
            os.mkdir(dest_dir)
            generate_page_recursive(content_dir, template_path, dest_dir)
    return
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as t:
        templ = t.read()
    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    html = templ.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)
    dest_folder = dest_path.split('/')[0]
    public_dir = os.path.join(os.getcwd(), dest_folder)
    os.makedirs(public_dir, exist_ok=True)
    w = open(dest_path, 'w')
    w.write(html)
    w.close()
