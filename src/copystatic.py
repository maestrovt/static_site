import os
import shutil

def copy_tree(src, target, log):
    list = os.listdir(src)
    if len(list) == 0:
        return log
    if not os.path.exists(target):
        os.mkdir(target)
    for item in list:
        src_path = os.path.join(src, item)
        if os.path.isfile(src_path):
            target_path = os.path.join(target, item)
            shutil.copy(src_path, target_path)
            log.append(f"Copying {src_path} to {target_path}")
        else:
            src_dir = os.path.join(src, item)
            target_dir = os.path.join(target, item)
            os.mkdir(target_dir)
            copy_tree(src_dir, target_dir, log)
    return log
