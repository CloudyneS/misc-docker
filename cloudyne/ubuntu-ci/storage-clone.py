#!/usr/bin/python3
"""
Clones one storage volume onto another in Kubernetes, with a lock file to prevent being overwritten
"""
import os
import shutil
import sys

def check_lock(path: str) -> bool:
    """Checks for the presence of a lock file in the directory

    Args:
        path (str): The path to check

    Returns:
        bool: If a lock file exists
    """
    return os.path.isfile(os.path.join(path, '.copy-lock'))


if __name__ == '__main__':
    if (
        (
            sys.argv[0] == "storage-clone" and
            len(sys.argv) < 3
        ) or (
            sys.argv[0] in ["python", "python3"] and
            len(sys.argv) < 4
        )):
        print('Usage: python3 storage-clone.py <source> <destination>')
        sys.exit(1)

    src_path = sys.argv[1] if sys.argv[0] == "storage-clone" else sys.argv[2] 
    dst_path = sys.argv[2] if sys.argv[0] == "storage-clone" else sys.argv[3]

    if not os.path.isdir(src_path) or not os.path.isdir(dst_path):
        print('One of the paths is not a directory')
        sys.exit(1)

    if check_lock(dst_path):
        print('Destination is locked, skipping copy')
        sys.exit(0)

    print('Copying {} to {}'.format(src_path, dst_path))
    shutil.copytree(src_path, dst_path)
