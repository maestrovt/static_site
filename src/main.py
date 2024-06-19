import os, shutil
from copystatic import copy_tree
from generate_page import generate_page_recursive
def main():
    src = "static"
    target = "public"
    log = []
    if os.path.exists(target):
        shutil.rmtree(target)
    log = copy_tree(src, target, log)
    with open("copy_log.txt", "w") as log_file:
        log_file.write("\n".join(log))
    print("\n".join(log))
    from_path_dir = "content"
    template_path = "template.html"
    dest_path_dir = "public"
    generate_page_recursive(from_path_dir, template_path, dest_path_dir)

    

main()
