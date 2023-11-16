from filecmp import dircmp
from shutil import copy, copytree, rmtree
import sys, os, platform
from threading import Thread

global OSNAME = platform.system()

def usablepath(path: str) -> str:
    path = path.strip()
    print(path)
    if OSNAME == "Linux" and not path.endswith('/'):
        path = path + "/"
    else if OSNAME == "Windows" and not path.endswith('\\')
        path = path + "\\"
    return path

# Check for file path formation.
def copy_diff_files_in_subdirs(dircmp_obj: dircmp, src: str, dest: str): 
    src = usablepath(src)
    dest = usablepath(dest)

    for dfs in dircmp_obj.diff_files:
        src_file_path = src + dfs
        dest_file_path = dest + dfs
        print("Copied diff files {} {}".format(src_file_path, dest_file_path))
        copy(src_file_path, dest_file_path)
    
    for key,value in dircmp_obj.subdirs.items():
        copy_diff_files_in_subdirs(value, src + key, dest + key) 
    
def remove_files_in_dest(dircmp_obj: dircmp, dest: str):
    # print the files in the right. 
    # print(dircmp_obj.right_only)
    dest = usablepath(dest)
    for fs in dircmp_obj.right_only:
        file_path = dest + fs
        print("Removed -> ", file_path)
        os.remove(file_path) if os.path.isfile(file_path) else rmtree(file_path, ignore_errors = True)

    for key, value in dircmp_obj.subdirs.items():
        remove_files_in_dest(value, dest + key)

def copy_files_added_to_source(dircmp_obj: dircmp, src: str, dest: str):
    src = usablepath(src)
    dest = usablepath(dest)
    for fs in dircmp_obj.left_only:
        src_file_path = src + fs
        dest_file_path = dest + fs
        print("Copied files {} {}".format(src_file_path, dest_file_path))
        copytree(src_file_path, dest_file_path, False, None) if os.path.isdir(src_file_path) else copy(src_file_path, dest_file_path)

    for dir_key in dircmp_obj.subdirs.keys():
        dir_val = dircmp_obj.subdirs[dir_key]
        copy_files_added_to_source(dir_val, src + dir_key, dest + dir_key)

def files_info(dircmp_obj: dircmp) -> dircmp:
    dircmp_obj.phase0()
    dircmp_obj.phase1()
    dircmp_obj.phase2()
    dircmp_obj.phase3()
    dircmp_obj.phase4()
    dircmp_obj.phase4_closure()
    return dircmp_obj


cmp= []
cmp.append(os.path.abspath(sys.argv[1]))
cmp.append(os.path.abspath(sys.argv[2]))


if len(cmp) < 2: 
    print("Command line arguments are enough less than 2, make sure the command line arguments are 2.")
    exit(1)

if not os.path.isdir(cmp[0]):
    print("The comparison is invalid as the source is a file")
    exit(1)

# copies the entire file tree. 
if not os.path.exists(cmp[1]):
    print("Destination folder does not exist, copying the entire path")
    copytree(cmp[0], cmp[1], False, None)
    exit(0)

dircmp_obj = dircmp(cmp[0], cmp[1])
dircmp_obj = files_info(dircmp_obj)

copy_diff_thread = Thread(target=copy_diff_files_in_subdirs, args = (dircmp_obj, cmp[0], cmp[1]))
copy_diff_thread.run()
remove_diff_thread = Thread(target=remove_files_in_dest, args = (dircmp_obj, cmp[1]))
remove_diff_thread.run()
copy_files_thread = Thread(target=copy_files_added_to_source, args = (dircmp_obj, cmp[0], cmp[1]))
copy_files_thread.run()

