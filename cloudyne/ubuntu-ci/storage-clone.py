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
    if len(sys.argv) < 2:
        print('Usage: python3 storage-clone.py <source> <destination>')
        print('Args: ', ' '.join(sys.argv))
        sys.exit(1)
    src_path = dst_path = ''
    
    if len(sys.argv) == 2 and sys.argv[0][0] == '/' and sys.argv[1][0] == '/':
        src_path = sys.argv[0]
        dst_path = sys.argv[1]
    
    elif len(sys.argv) == 3 and sys.argv[1][0] == '/' and sys.argv[2][0] == '/':
        src_path = sys.argv[1]
        dst_path = sys.argv[2]
    
    elif len(sys.argv) == 3 and sys.argv[2][0] == '/' and sys.argv[3][0] == '/':
        src_path = sys.argv[2]
        dst_path = sys.argv[3]
        
    else:
        print('Usage: python3 storage-clone.py <source> <destination>')
        print('Args: ', ' '.join(sys.argv))
        sys.exit(1)

    if not os.path.isdir(src_path) or not os.path.isdir(dst_path):
        print('One of the paths is not a directory')
        sys.exit(1)

    if check_lock(dst_path):
        print('Destination is locked, skipping copy')
        sys.exit(0)

    print(f'Copying {src_path} to {dst_path}')
    shutil.copytree(src_path, dst_path)

    print("Creating lock file...")
    with open(os.path.join(dst_path, '.copy-lock'), 'w', encoding='utf-8') as lock_file:
        lock_file.write('locked')

    print('Finished copying')
    sys.exit(0)
