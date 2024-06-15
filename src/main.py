import os, shutil
from copystatic import copy_tree
from generate_page import generate_page
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
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    generate_page(from_path, template_path, dest_path)

    

main()
