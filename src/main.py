import os, shutil
from copystatic import copy_tree
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

    

main()
